# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    escola = fields.Char(string="Escola", compute="_compute_escola")
    rel_user_id = fields.Many2one('res.users', compute="_compute_usuari", string="Usuari relacionat")
    mobile = fields.Char(compute="_compute_mobile")
    street = fields.Char(compute="_compute_street")
    street2 = fields.Char(compute="_compute_street2")
    zip = fields.Char(change_default=True, compute="_compute_zip")
    city = fields.Char(compute="_compute_city")
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', compute="_compute_state_id")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', compute="_compute_country_id")

    def _compute_usuari(self):
        for record in self:
            if record.env['res.users'].search([('partner_id','=',self.id)]).escola != False:
                record.rel_user_id = record.env['res.users'].search([('partner_id','=',self.id)])

    @api.depends('re_user_id')
    def _compute_escola(self):
        for record in self:
            record.escola = record.rel_user_id.escola

    @api.depends('re_user_id')
    def _compute_mobile(self):
        for record in self:
            record.mobile = record.rel_user_id.mobile

    @api.depends('re_user_id')
    def _compute_street(self):
        for record in self:
            record.street = record.rel_user_id.street

    @api.depends('re_user_id')
    def _compute_street2(self):
        for record in self:
            record.street2 = record.rel_user_id.street2
    
    @api.depends('re_user_id')
    def _compute_zip(self):
        for record in self:
            record.zip = record.rel_user_id.zip

    @api.depends('re_user_id')
    def _compute_city(self):
        for record in self:
            record.city = record.rel_user_id.city

    @api.depends('re_user_id')
    def _compute_country_id(self):
        for record in self:
            record.country_id = record.rel_user_id.country_id

    @api.depends('re_user_id')
    def _compute_state_id(self):
        for record in self:
            record.state_id = record.rel_user_id.state_id
