# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    escola = fields.Char()

    name = fields.Char(index=True, compute="get_name")

    @api.depends('firstname')
    def get_name(self):
        if self.name == "":
            self.name = self.firstname + " " + self.lastname

    """@api.depends('escola')
    def assignar_cmontserrat(self):
        """