from odoo import api, models, fields, _


class TanAccountMoveLine(models.Model):

    _inherit = 'account.move.line'


    sequence = fields.Integer('Sequence No.', compute="_compute_sequence", default=0)


    @api.depends('move_id.invoice_line_ids', 'move_id.invoice_line_ids.product_id')
    def _compute_sequence(self):
        for line in self:
            no = 0
            line.sequence = no
            for l in line.move_id.invoice_line_ids:
                no += 1
                l.sequence = no
