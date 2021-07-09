# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class repair_line(models.Model):
    _inherit = 'mrp.repair.line'

    pieza_añadida = fields.Boolean('Pieza añadida?')

    @api.multi
    def action_set_pieza_añadida(self):
        self.ensure_one()
        self.pieza_añadida = not self.pieza_añadida
        print(self.pieza_añadida)