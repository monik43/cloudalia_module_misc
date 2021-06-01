# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    escola = fields.Char()