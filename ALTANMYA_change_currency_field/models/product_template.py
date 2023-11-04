from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        related='company_id.currency_id',  # You can customize this based on your needs.
        store=True,  # This makes the field stored.
        readonly=True,  # You can make it read-only if needed.
    )
