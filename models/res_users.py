# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class resusers(models.Model):
    _inherit = 'res.users'
    """
    mobile = fields.Char(store=True)
    vat = fields.Char(store=True)
    street = fields.Char(store=True)
    street2 = fields.Char(store=True)
    zip = fields.Char(store=True)
    city = fields.Char(store=True)
    state_id = fields.Many2one("res.country.state", string='State', store=True)
    country_id = fields.Many2one('res.country', string='Country')
    escola = fields.Char(store=True)"""
