# -*- coding: utf-8 -*-
from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_on_sale = fields.Boolean(
        string="En Oferta",
        help="Marcar para mostrar este producto como 'Oferta' en los filtros de la tienda.",
        index=True  # indexamos para mejorar el rendimiento de las búsquedas
    )