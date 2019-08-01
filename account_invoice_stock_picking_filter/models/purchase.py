# -*- coding: utf-8 -*-

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.depends('order_id.state', 'move_ids.state',
                 'move_ids.product_uom_qty')
    def _compute_qty_received(self):
        if self._context.get("picking_ids"):
            pick_ids = self._context.get("picking_ids")
            for line in self:
                if line.order_id.state not in ['purchase', 'done']:
                    line.qty_received = 0.0
                    continue
                if line.product_id.type not in ['consu', 'product']:
                    line.qty_received = line.product_qty
                    continue
                total = 0.0
                move_ids = line.move_ids
                moves = move_ids.filtered(lambda m: m.picking_id.id in pick_ids
                                                    and m.state == 'done')
                for move in moves:
                    if move.location_dest_id.usage == "supplier":
                        if move.to_refund:
                            total -= move.product_uom._compute_quantity(
                                move.product_uom_qty, line.product_uom)
                    else:
                        total += move.product_uom._compute_quantity(
                            move.product_uom_qty, line.product_uom)
                line.qty_received = total
        else:
            super(PurchaseOrderLine, self)._compute_qty_received()
