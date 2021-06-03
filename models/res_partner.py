# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    escola = fields.Char(compute="_assignar_escola")
    user_id = fields.Many2one('res.users', compute="_assignar_usuari")

    @api.depends('user_id')
    def _assignar_escola(self):
        for record in self:
            record.escola = record.user_id.escola

    def _assignar_usuari(self):

        for record in self:
            record.user_id = record.env['res.users'].search([('partner_id','=',self.id)])
            print(record.user_id, "#/"*50)