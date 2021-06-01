# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    escola_associada = fields.Many2One(compute="_get_escola_from_user")

    @api.depends('payment_responsible_id')
    def _get_escola_from_user(self):
        user = self.env['res.users'].search([('id','=',self.payment_responsible_id)])
        if user.escola == 'cmontserrat_c':
            self.escola_associada = self.env['res.partner'].search([('id','=','16923')])
