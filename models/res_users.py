# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class resusers(models.Model):
    _inherit = 'res.users'

    phone = fields.Char()
    vat = fields.Char()
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    country_id = fields.Char()
    state_id = fields.Char()
    escola = fields.Char()