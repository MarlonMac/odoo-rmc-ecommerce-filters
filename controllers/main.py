# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleRMC(WebsiteSale):

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth="public", website=True, sitemap=WebsiteSale.sitemap_shop)
    def shop(self, page=0, category=None, search='', ppg=False, ppl=False, **post):
        # 1. Obtenemos la respuesta y el contexto base del controlador original.
        # Es importante pasar 'search' y 'category' para que se apliquen los filtros nativos.
        # 'category' puede venir en 'post' si se usa el select en lugar de la URL.
        if post.get('category'):
            try:
                category = request.env['product.public.category'].browse(int(post.get('category')))
            except (ValueError, TypeError):
                pass
        
        response = super(WebsiteSaleRMC, self).shop(page=page, category=category, search=search, ppg=ppg, ppl=ppl, **post)
        
        # 2. Obtenemos el dominio de búsqueda ya construido por el 'super'.
        domain = response.qcontext.get('search_domain', [])
        
        # 3. Añadimos nuestro filtro de "Ofertas" si está activo.
        is_on_sale_checked = bool(post.get('on_sale'))
        if is_on_sale_checked:
            # Añadimos nuestra condición al dominio existente
            domain.append(('is_on_sale', '=', True))
        
        # 4. Con el dominio final, recalculamos los productos y el paginador si es necesario.
        # Esto solo se ejecuta si hemos modificado el dominio.
        if is_on_sale_checked:
            Product = request.env['product.template'].with_context(bin_size=True)
            
            # Obtenemos los argumentos de la URL actual para el paginador
            url_args = dict(request.httprequest.args)
            
            product_count = Product.search_count(domain)
            pager = request.website.pager(
                url=request.httprequest.path.split('/page/')[0],
                total=product_count,
                page=page,
                step=response.qcontext['ppg'],
                scope=7,
                url_args=url_args,
            )
            products = Product.search(domain, limit=ppg, offset=pager['offset'], order=self._get_search_order(post))
            
            # Actualizamos el contexto de la respuesta
            response.qcontext.update({
                'products': products,
                'product_count': product_count,
                'pager': pager,
                'search_domain': domain, # Actualizamos el dominio en el contexto
            })

        # 5. Siempre pasamos el estado del checkbox a la vista.
        response.qcontext['is_on_sale_checked'] = is_on_sale_checked
        
        return response