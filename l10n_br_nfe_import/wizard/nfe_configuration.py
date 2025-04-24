from odoo import api, fields, models
from odoo.exceptions import UserError


class WizardNFeConfiguration(models.TransientModel):
    _name = "wizard.nfe.configuration"
    _description = "Wizard Configuracao NFe"

    eletronic_doc_id = fields.Many2one("eletronic.document")
    partner_id = fields.Many2one("res.partner", string="Parceiro")  

    create_all_products = fields.Boolean(
        string="Criar os produtos?", 
        help="Se marcado vai criar os produtos não encontrados")

    currency_id = fields.Many2one(related='eletronic_doc_id.currency_id')

    nfe_number = fields.Integer(related="eletronic_doc_id.numero")
    amount_total = fields.Monetary(related="eletronic_doc_id.valor_final")

    nfe_item_ids = fields.One2many('wizard.nfe.configuration.item', 'wizard_id')
    
    @api.onchange('create_all_products')
    def _onchange_create_all_products(self):
        for item in self.nfe_item_ids:
            item.create_products = self.create_all_products
            
    
    def action_confirm_items(self):
        for item in self.nfe_item_ids:
            if item.create_products:
                product = self.env['product.product'].create({
                    'name': item.xml_product_name,
                    'purchase_ok': True,
                    'sale_ok': False,
                    'type': 'product',
                    'list_price': item.price_total / item.quantity,
                    # 'l10n_br_fiscal_category_id':'Venda de produto',
                    # 'l10n_br_origin': 0,
                    'taxes_id': [],
                    'supplier_taxes_id': [],
                    'company_id': None,
                    ### JUNIOR
                    'barcode': item.xml_product_ean,
                    'l10n_br_origin': item.xml_origem,
                    'l10n_br_ncm_id': self.env['account.ncm'].search([('code', '=', item.xml_ncm_code)], limit=1).id,
                    'l10n_br_cest': item.xml_cest,
                    'product_prod_anvisa': item.xml_product_prod_anvisa,
                    'product_pmc': item.xml_product_pmc,

                })
                item.product_id = product
                item.uom_id = product.uom_id
                
                self.env['product.supplierinfo'].create({
                    'product_id': product.id,
                    'product_tmpl_id': product.product_tmpl_id.id,
                    'name': self.partner_id.id,
                    'product_code': item.xml_product_code,
                    'product_name': item.xml_product_name,
                    'barcode': item.xml_product_ean,
                })


            if not item.product_id or not item.uom_id:
                raise UserError('Configure todos os produtos para continuar')
        
            item.eletronic_line_id.product_id = item.product_id.id
            item.eletronic_line_id.uom_id = item.uom_id.id
        
        return {
            "type": "ir.actions.act_window",
            "res_model": "eletronic.document",
            "view_mode": "tree,form",
            'view_type': 'form',
            'views': [[False, 'form']],
            "name": "Nota Fiscal Eletrônica",
            "res_id": self.eletronic_doc_id.id,
        }


class WizardNFeConfigurationItem(models.TransientModel):
    _name = "wizard.nfe.configuration.item"
    _description = "Wizard Configuracao NFe Item"

    wizard_id = fields.Many2one('wizard.nfe.configuration')
    create_products = fields.Boolean(string='Criar?', 
        help="Se marcado vai criar os produtos não encontrados")
    product_id = fields.Many2one("product.product")
    uom_id = fields.Many2one("uom.uom")
    
    eletronic_line_id = fields.Many2one("eletronic.document.line")
    currency_id = fields.Many2one(related='eletronic_line_id.currency_id')
    quantity = fields.Float(related='eletronic_line_id.quantidade')
    price_total = fields.Monetary(related="eletronic_line_id.valor_liquido")
    xml_product_code = fields.Char(related="eletronic_line_id.product_cprod", string="Cód.") ###
    xml_product_name = fields.Char(related="eletronic_line_id.product_xprod")
    xml_uom_code = fields.Char(related="eletronic_line_id.unidade_medida", string="Un.")
    xml_ncm_code = fields.Char(related="eletronic_line_id.ncm") ###
    xml_cfop = fields.Char(related="eletronic_line_id.cfop")

    #### JUNIOR ####
    xml_product_ean = fields.Char(related="eletronic_line_id.product_ean")
    xml_cest = fields.Char(related="eletronic_line_id.cest")
    xml_product_prod_anvisa = fields.Char(related="eletronic_line_id.product_prod_anvisa")
    xml_product_pmc = fields.Float(related="eletronic_line_id.product_pmc")
    xml_origem = fields.Selection(related="eletronic_line_id.origem")

