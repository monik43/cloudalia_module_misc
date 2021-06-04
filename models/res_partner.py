# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    escola = fields.Char(string="Escola", compute="_assignar_escola")
    rel_user_id = fields.Many2one('res.users', compute="_assignar_usuari", string="Usuari relacionat")

    

    def _assignar_usuari(self):
        for record in self:
            record.rel_user_id = record.env['res.users'].search([('partner_id','=',self.id)])

    def _assignar_escola(self):
        for record in self:
            record.escola = record.rel_user_id.escola