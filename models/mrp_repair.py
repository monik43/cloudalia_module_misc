# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class repair_line(models.Model):
    _inherit = 'mrp.repair.line'

    pieza_añadida = fields.Boolean('Pieza añadida?')

    @api.multi
    def action_set_pieza_añadida(self):
        for record in self:
            record.pieza_añadida = not record.pieza_añadida
            print(record.pieza_añadida)