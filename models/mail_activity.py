# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class mail_activity(models.Model):
    _inherit = 'mail.activity'

    filtro_check = fields.Boolean('Habilitar usuarios externos?')

    @api.onchange('filtro_check')
    def onchange_filtro_check(self):
        for record in self:
            if record.filtro_check:
                domain = [('firstname','!=',False)]
            else:
                domain = [('share','=',False)]
            return {'domain':{'user_id':domain}}