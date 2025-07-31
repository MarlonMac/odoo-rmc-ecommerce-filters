# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleRMC(WebsiteSale):

    @http.route(['/shop/subcategories'], type='json', auth="public", website=True)
    def get_subcategories(self, category_id=None):
        if not category_id:
            return []
        try:
            from odoo.addons.http_routing.models.ir_http import slug

            subcategories = request.env['product.public.category'].search([
                ('parent_id', '=', int(category_id))
            ])
            return [{'id': sub.id, 'name': sub.name, 'slug': slug(sub)} for sub in subcategories]
        except (ValueError, TypeError):
            return []

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, ppl=False, **post):
        # Llamamos al método padre que maneja todo el flujo básico
        response = super(WebsiteSaleRMC, self).shop(page=page, category=category, search=search, ppg=ppg, ppl=ppl, **post)

        domain = response.qcontext.get('search_domain', [])
        domain_modified = False
        
        # Filtro personalizado: 'En oferta'
        is_on_sale_checked = bool(post.get('on_sale'))
        if is_on_sale_checked:
            domain.append(('is_on_sale', '=', True))
            domain_modified = True
        
        # Filtro personalizado: Rango de precios
        min_price = post.get('min_price')
        max_price = post.get('max_price')
        price_filter_active = False
        
        if min_price:
            try:
                min_price_float = float(min_price)
                if min_price_float > 0:
                    domain.append(('list_price', '>=', min_price_float))
                    domain_modified = True
                    price_filter_active = True
            except (ValueError, TypeError):
                min_price = None
                
        if max_price:
            try:
                max_price_float = float(max_price)
                if max_price_float > 0:
                    domain.append(('list_price', '<=', max_price_float))
                    domain_modified = True
                    price_filter_active = True
            except (ValueError, TypeError):
                max_price = None
        
        # Si hemos modificado el dominio, recalculamos los productos
        if domain_modified:
            Product = request.env['product.template'].with_context(bin_size=True)
            product_count = Product.search_count(domain)
            
            if product_count > 0:
                pager = request.website.pager(
                    url=request.httprequest.path.split('/page/')[0],
                    total=product_count,
                    page=page,
                    step=response.qcontext['ppg'],
                    scope=7,
                    url_args=request.httprequest.args,
                )
                products = Product.search(
                    domain, 
                    limit=response.qcontext['ppg'], 
                    offset=pager['offset'], 
                    order=self._get_search_order(post)
                )
                
                response.qcontext.update({
                    'products': products,
                    'product_count': product_count,
                    'pager': pager,
                    'search_domain': domain,
                })
            else:
                # Si no hay productos, mostramos un resultado vacío pero válido
                response.qcontext.update({
                    'products': Product.browse([]),
                    'product_count': 0,
                    'search_domain': domain,
                })

        # Detectar si hay filtros activos
        filters_active = bool(
            category or 
            is_on_sale_checked or 
            price_filter_active
        )
        
        response.qcontext.update({
            'is_on_sale_checked': is_on_sale_checked,
            'filters_active': filters_active,
        })
        
        # Mantener estado de categorías para los selects
        current_category = category
        if current_category and current_category.parent_id:
             response.qcontext['selected_parent_category_id'] = current_category.parent_id.id
             response.qcontext['selected_subcategory_id'] = current_category.id
        elif current_category:
             response.qcontext['selected_parent_category_id'] = current_category.id
        
        return response