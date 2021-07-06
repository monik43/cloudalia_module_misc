# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class resusers(models.Model):
    _inherit = 'res.users'

    mobile = fields.Char()
    vat = fields.Char()
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(
        "res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    escola = fields.Char()
