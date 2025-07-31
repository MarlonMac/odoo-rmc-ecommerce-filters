# -*- coding: utf-8 -*-
{
    'name': "Red Music Corporation - eCommerce Filters",
    'summary': """
        Agrega un bloque de filtros avanzado y minimalista a la página de la tienda.
        Permite filtrar por categoría, subcategoría, productos en oferta y rango de precios.
    """,
    'description': """
        Este módulo mejora la experiencia del usuario en la tienda en línea (eCommerce)
        al añadir un bloque de filtros personalizable justo debajo de la barra de búsqueda.
        Los filtros disponibles son:
        - Categoría y Subcategoría de producto (navegación dinámica)
        - Productos en Oferta (interruptor)
        - Rango de Precios (slider nativo de Odoo)
    """,
    'author': "Marlon Macario para Red Music Corporation",
    'website': "https://www.link-gt.com",
    'category': 'Website/eCommerce',
    'version': '16.0.2.0',
    'license': 'LGPL-3',
    'depends': [
        'product',
        'website',
        'website_sale',
        # 'product_brand_sale',  # Descomentado si se requiere compatibilidad con marcas,
        ],
    'data': [
        'views/product_template_views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'rmc_ecommerce_filters/static/src/css/rmc_ecommerce_filters.css',
            'rmc_ecommerce_filters/static/src/js/rmc_ecommerce_filters.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}