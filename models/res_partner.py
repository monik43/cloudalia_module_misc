# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class respartner(models.Model):
    _inherit = 'res.partner'

    acces_botiga = fields.Boolean(default=False, string="Acces a la botiga?")