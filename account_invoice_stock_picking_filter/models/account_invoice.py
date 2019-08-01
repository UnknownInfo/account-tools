# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.float_utils import float_compare
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    picking_ids = fields.Many2many(comodel_name="stock.picking",
                                   string="Albaranes")

    @api.onchange("picking_ids")
    def onchange_pickings(self):
        if self.picking_ids:
            purchases = []
            for picking_id in self.picking_ids:
                if not picking_id.purchase_id.id in purchases:
                    purchases.append(picking_id.purchase_id.id)
            if len(purchases) > 0:
                # self.invoice_line_ids = False
                for purchase in purchases:
                    self.purchase_id = purchase
                    self.purchase_order_change()

    def _prepare_invoice_line_from_po_line(self, line):
        res = super(AccountInvoice, self)._prepare_invoice_line_from_po_line(
            line)
        if self.picking_ids:
            if line.product_id.purchase_method == 'purchase':
                qty = line.product_qty - line.qty_invoiced
            else:
                qty = line.with_context(
                    {'picking_ids': self.picking_ids.ids}).qty_received
                # if not self.picking_ids:
                #     qty = qty - line.qty_invoiced
            value = float_compare(
                qty, 0.0, precision_rounding=line.product_uom.rounding)
            if value <= 0:
                qty = 0.0
            res.update({'quantity': qty})
        return res

    @api.onchange('purchase_id')
    def purchase_order_change(self):
        if not self.purchase_id:
            return {}
        if not self.partner_id:
            self.partner_id = self.purchase_id.partner_id.id

        vendor_ref = self.purchase_id.partner_ref
        if vendor_ref and (not self.reference or (
                vendor_ref + ", " not in self.reference and not self.reference.endswith(vendor_ref))):
            self.reference = ", ".join([self.reference, vendor_ref]) if self.reference else vendor_ref

        new_lines = self.env['account.invoice.line']
        valid_products = self.purchase_id.mapped('order_line').mapped('product_id')
        if self.picking_ids:
            valid_products = self.picking_ids.mapped('move_lines').mapped('product_id')

        for line in self.purchase_id.order_line - self.invoice_line_ids.mapped('purchase_line_id'):
            if line.product_id in valid_products:
                data = self._prepare_invoice_line_from_po_line(line)
                new_line = new_lines.new(data)
                new_line._set_additional_fields(self)
                new_lines += new_line

        self.invoice_line_ids += new_lines
        self.payment_term_id = self.purchase_id.payment_term_id
        self.env.context = dict(self.env.context, from_purchase_order_change=True)
        self.purchase_id = False
        return {}
