# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging

from ast import literal_eval

from odoo.exceptions import UserError
from odoo.tools.misc import ustr

from odoo.addons.base.ir.ir_mail_server import MailDeliveryException
from odoo.addons.auth_signup.models.res_partner import SignupError, now


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
