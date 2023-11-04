from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=True,
        store=True,
    )
