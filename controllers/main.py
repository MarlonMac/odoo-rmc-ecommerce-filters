# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleRMC(WebsiteSale):

    # CORRECCIÓN 1: Devolvemos también el 'slug' de la categoría.
    @http.route(['/shop/subcategories'], type='json', auth="public", website=True)
    def get_subcategories(self, category_id=None):
        if not category_id:
            return []
        try:
            # La función 'slug' nos ayuda a crear la parte de la URL amigable.
            from odoo.addons.http_routing.models.ir_http import slug

            subcategories = request.env['product.public.category'].search([
                ('parent_id', '=', int(category_id))
            ])
            # Devolvemos un diccionario con id, nombre y el slug.
            return [{'id': sub.id, 'name': sub.name, 'slug': slug(sub)} for sub in subcategories]
        except (ValueError, TypeError):
            return []

    # CORRECCIÓN 2: El método 'shop' se simplifica drásticamente.
    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, ppl=False, **post):
        # El filtrado por categoría/subcategoría ahora lo hace Odoo de forma nativa a través de la URL.
        # Ya no necesitamos procesar 'category' o 'subcategory' desde el 'post'.
        
        response = super(WebsiteSaleRMC, self).shop(page=page, category=category, search=search, ppg=ppg, ppl=ppl, **post)

        domain = response.qcontext.get('search_domain', [])
        is_on_sale_checked = bool(post.get('on_sale'))
        domain_modified = False
        
        # El único filtro personalizado que debemos manejar es 'En oferta'.
        if is_on_sale_checked:
            domain.append(('is_on_sale', '=', True))
            domain_modified = True
            
        if domain_modified:
            Product = request.env['product.template'].with_context(bin_size=True)
            product_count = Product.search_count(domain)
            pager = request.website.pager(
                url=request.httprequest.path.split('/page/')[0],
                total=product_count,
                page=page,
                step=response.qcontext['ppg'],
                scope=7,
                url_args=request.httprequest.args,
            )
            products = Product.search(domain, limit=ppg, offset=pager['offset'], order=self._get_search_order(post))
            
            response.qcontext.update({
                'products': products,
                'product_count': product_count,
                'pager': pager,
                'search_domain': domain,
            })

        # Lógica de indicador de filtros activos (simplificada).
        # Se activa si estamos en una página de categoría o si el filtro de ofertas está marcado.
        filters_active = bool(category or is_on_sale_checked)
        
        response.qcontext['is_on_sale_checked'] = is_on_sale_checked
        response.qcontext['filters_active'] = filters_active
        
        # Pasamos la categoría actual para mantener el estado del <select> de categoría padre.
        current_category = category
        if current_category and current_category.parent_id:
             response.qcontext['selected_parent_category_id'] = current_category.parent_id.id
             response.qcontext['selected_subcategory_id'] = current_category.id
        elif current_category:
             response.qcontext['selected_parent_category_id'] = current_category.id
        
        return response