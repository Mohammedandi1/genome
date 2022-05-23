from odoo import api, fields, models



class AccountMoveLineExt(models.Model):
    _inherit = "account.move.line"

    gross_amount = fields.Float(string='Gross Amount', compute='_compute_gross_amount')
    discount_amount = fields.Float(string='Discount Amount', compute='_compute_discount_amount')


    @api.depends("price_unit","quantity")
    def _compute_gross_amount(self):
        for rec in self:
            rec.gross_amount = rec.price_unit * rec.quantity

    @api.depends("gross_amount", "discount")
    def _compute_discount_amount(self):
        for rec in self:
            disc = rec.discount
            if rec.discount > 0:
                disc = rec.discount / 100.0
            rec.discount_amount = rec.gross_amount * disc



class AccountMoveExt(models.Model):
    _inherit = "account.move"

    total_gross_amount = fields.Float(string='Total Gross Amount', compute='_compute_total_gross_amount')
    total_discount_amount = fields.Float(string='Total Discount Amount', compute='_compute_total_discount_amount')


    @api.depends("line_ids.price_unit","line_ids.quantity","line_ids.gross_amount")
    def _compute_total_gross_amount(self):
        for rec in self:
            rec.total_gross_amount = 0.0
            for line in rec.invoice_line_ids:
                rec.total_gross_amount += line.gross_amount

    @api.depends("line_ids.gross_amount","line_ids.discount","line_ids.discount_amount")
    def _compute_total_discount_amount(self):
        for rec in self:
            rec.total_discount_amount = 0.0
            for line in rec.invoice_line_ids:
                rec.total_discount_amount += line.discount_amount
