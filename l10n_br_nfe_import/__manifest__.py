{  # pylint: disable=C8101,C8103
    "name": "Importação de Documento Fiscal Eletronico",
    "version": "13.0.1.0.1",
    "category": "Account addons",
    "license": "AGPL-3",
    "author": "Trustcode",
    "website": "http://www.trustcode.com.br",
    "description": """
        Implementa funcionalidade para importar xml da nfe.""",
    "contributors": [
        "Danimar Ribeiro <danimaribeiro@gmail.com>",
    ],
    "depends": ["sale", "l10n_br_eletronic_document", "nds_product_anp"],
    "data": [
        "data/payment_term.xml",
        "data/product.xml",
        "security/ir.model.access.csv",
        "views/res_config_settings.xml",
        "views/invoice_eletronic.xml",
        "views/product_category.xml",
        "views/product_view.xml",
        "wizard/import_nfe.xml",
        "wizard/nfe_configuration.xml",
        "wizard/xml_import.xml",
    ],
    "installable": True,
}
