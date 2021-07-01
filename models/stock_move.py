# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class stockmove(models.Model):
    _inherit = 'stock.move'

    ship_order_move = fields.Char(compute="_get_purchase_ship_order")

    @api.depends('picking_id')
    def _get_purchase_ship_order(self):

        for record in self:
            stock_picking = record.env['stock.picking']

            if stock_picking.browse(record.picking_id.id):

                record.ship_order_move = stock_picking.browse(
                    record.picking_id.id).purchase_ship_order
