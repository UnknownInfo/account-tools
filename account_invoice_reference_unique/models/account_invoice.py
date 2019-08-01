# -*- coding: utf-8 -*-
# (c) 2019 Praxya - Miquel March <mmarch@praxya.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.one
    @api.constrains('reference')
    def _check_reference_uniq(self):
        if self.reference:
            invoices = self.env['account.invoice'].search(
                [
                    ('id', '!=', self.id),
                    ('reference', '=', self.reference),
                    ('partner_id', '=', self.partner_id.id),
                 ]
            )
            if len(invoices) > 0:
                raise ValidationError(
                    'Se detectó una referencia duplicada del proveedor.')
