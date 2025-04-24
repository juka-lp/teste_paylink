# © 2023 Junior Lopes - NDS Sistemas

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_prod_anvisa = fields.Char('Cód. Produto ANVISA')
    product_pmc = fields.Float('Preço Máximo Consumidor (PMC)')
