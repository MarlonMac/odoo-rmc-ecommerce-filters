# -*- coding: utf-8 -*-
{
    'name': "Red Music Corporation - eCommerce Filters",
    'summary': """
        Agrega un bloque de filtros avanzado y minimalista a la página de la tienda.
        Permite filtrar por categoría, marca, productos destacados y rango de precios.
    """,
    'description': """
        Este módulo mejora la experiencia del usuario en la tienda en línea (eCommerce)
        al añadir un bloque de filtros personalizable justo debajo de la barra de búsqueda.
        Los filtros disponibles son:
        - Categoría de producto (menú desplegable)
        - Marca (campo del módulo product_brand_sale)
        - Productos Destacados
        - Rango de Precios
    """,
    'author': "Marlon Macario para Red Music Corporation",
    'website': "https://www.link-gt.com",
    'category': 'Website/eCommerce',
    'version': '16.0.1.0.3',
    'license': 'LGPL-3',
    'depends': [
        'product',
        'website',
        'website_sale',
        'product_brand_sale', # Dependencia para marcas de productos 
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