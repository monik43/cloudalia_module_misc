# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import float_is_zero


class productproduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def print(self):
        print(self.warehouse_id)
        for record in self:
            print(record.warehouse_id)