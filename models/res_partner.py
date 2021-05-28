# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class respartner(models.Model):
    _inherit = 'res.partner'



    usuari_associat = fields.Many2one('res.user')
    escola = fields.Char(string="Tenda de l'escola", compute="_get_escola_from_user")
    #acces_botiga = fields.Boolean(default=False, string="Acces a la botiga?")

    @api.depends('email')
    def _get_escola_from_user(self):
        escola = self.env['res.users'].search(['login', '=', self.email])
