import logging

from deep_translator import GoogleTranslator

from odoo import api, fields, models


_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None


class SaleOrderSpelling(models.Model):
    _inherit = "sale.order"

    spelling_total_en = fields.Text(compute="_compute_spelling_en", string="Spelling English")
    spelling_total_ar = fields.Text(compute="_compute_spelling_ar", string="Spelling Arabic")

    def get_total_from_invoice_info(self, invoice_info):
        if invoice_info:
            return round(invoice_info.get("total_amount", 0.0), 2)
        return False

    def get_spelling_num(self, num: float, lang="en", currency_unit="Dollars", currency_subunit="Cents"):
        if not num2words:
            return ""

        integer_part = int(num)
        decimal_part = int(round((num - integer_part) * 100))

        if lang == "en":
            integer_spell = num2words(integer_part, lang="en") + " " + currency_unit
            decimal_spell = num2words(decimal_part, lang="en") + " " + currency_subunit
            return f"{integer_spell} And {decimal_spell}".title()

        elif lang == "ar":
            integer_spell = num2words(integer_part, lang="ar") + " " + currency_unit
            decimal_spell = num2words(decimal_part, lang="ar") + " " + currency_subunit
            return f"{integer_spell} و {decimal_spell}"

        return ""

    @api.depends("tax_totals")
    def _compute_spelling_en(self):
        for order in self:
            order.spelling_total_en = ""
            total = order.get_total_from_invoice_info(order.tax_totals)
            if total:
                en_currency_unit = order.currency_id.currency_unit_label
                en_currency_subunit = order.currency_id.currency_subunit_label
                order.spelling_total_en = order.get_spelling_num(
                    total, lang="en", currency_unit=en_currency_unit, currency_subunit=en_currency_subunit
                )

    @api.depends("tax_totals")
    def _compute_spelling_ar(self):
        for order in self:
            order.spelling_total_ar = ""
            total = order.get_total_from_invoice_info(order.tax_totals)
            if total:
                ar_currency_unit = GoogleTranslator(source="auto", target="ar").translate(
                    order.currency_id.currency_unit_label
                )
                ar_currency_subunit = GoogleTranslator(source="auto", target="ar").translate(
                    order.currency_id.currency_subunit_label
                )

                # Manual overrides for specific currencies
                if order.currency_id.id == 136:
                    ar_currency_unit = "ليرة سورية"
                    ar_currency_subunit = "قرش"
                elif order.currency_id.id == 90:
                    ar_currency_unit = "دينار أردني"
                    ar_currency_subunit = "قرش"

                order.spelling_total_ar = order.get_spelling_num(
                    total, lang="ar", currency_unit=ar_currency_unit, currency_subunit=ar_currency_subunit
                )
