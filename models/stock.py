# -*- coding: utf-8 -*-

from odoo import models, fields, api


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    purchase_ship_order = fields.Char(compute="_get_ship_order")

    @api.depends('purchase_id')
    def _get_ship_order(self):

        for record in self:

            if record.purchase_id.ship_order:

                record.purchase_ship_order = record.purchase_id.ship_order

    @api.multi
    def fill_all_product_quantities(self):
        
        for o in self.move_line_ids:
            """
            if product.quantity_done < product.product_uom_qty:
                product.quantity_done = product.product_uom_qty
            """
            print("" + str(o.qty_done))
            print("#" * 25)
            print("" + str(o.product_qty))
            print("#" * 25)

        




class stockmove(models.Model):
    _inherit = 'stock.move'

    ship_order_move = fields.Char(compute="_get_purchase_ship_order")

    @api.depends('picking_id')
    def _get_purchase_ship_order(self):

        for record in self:
            stock_picking = record.env['stock.picking']

            if stock_picking.browse(record.picking_id.id):

                record.ship_order_move = stock_picking.browse(record.picking_id.id).purchase_ship_order
