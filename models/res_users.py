# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class resusers(models.Model):
    _inherit = 'res.users'

    escola = fields.Char()
