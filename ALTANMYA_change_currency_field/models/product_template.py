from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        related=False,  # You can customize this based on your needs.
        store=True,  # This makes the field stored.
        readonly=False,  # You can make it read-only if needed.
    )
