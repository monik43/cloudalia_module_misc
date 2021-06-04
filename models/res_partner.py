# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    rel_user_id = fields.Many2one("res.users", compute="_compute_usuari")

    escola = fields.Char(string="Escola", compute="_compute_escola")
    mobile = fields.Char(compute="_compute_mobile")
    street = fields.Char(compute="_compute_street")
    street2 = fields.Char(compute="_compute_street2")
    zip = fields.Char(change_default=True, compute="_compute_zip")
    city = fields.Char(compute="_compute_city")
    state_id = fields.Many2one(
        "res.country.state", string='State', ondelete='restrict', compute="_compute_state_id")
    #country_id = fields.Many2one(    "res.country", string='Country', compute="_compute_country_id")
    vat = fields.Char(string='TIN', help="Tax Identification Number. "
                                         "Fill it if the company is subjected to taxes. "
                                         "Used by the some of the legal statements.", compute="_compute_vat")

    def _compute_usuari(self):
        for record in self:
            if record.env['res.users'].search([('partner_id', '=', record.id)]).escola != False:
                record.rel_user_id = record.env['res.users'].search([('partner_id', '=', record.id)])

    @api.depends('rel_user_id')
    def _compute_escola(self):
        for record in self:
            if record.env['res.users'].search([('partner_id', '=', record.id)]).escola != False:
                record.escola = record.rel_user_id.escola

    @api.depends('rel_user_id')
    def _compute_mobile(self):
        for record in self:
            record.mobile = record.rel_user_id.mobile

    @api.depends('rel_user_id')
    def _compute_street(self):
        for record in self:
            record.street = record.rel_user_id.street

    @api.depends('rel_user_id')
    def _compute_street2(self):
        for record in self:
            record.street2 = record.rel_user_id.street2

    @api.depends('rel_user_id')
    def _compute_zip(self):
        for record in self:
            record.zip = record.rel_user_id.zip

    @api.depends('rel_user_id')
    def _compute_city(self):
        for record in self:
            record.city = record.rel_user_id.city

    @api.depends('rel_user_id')
    def _compute_state_id(self):
        for record in self:
            record.state_id = record.rel_user_id.state_id

    @api.depends('rel_user_id')
    def _compute_vat(self):
        for record in self:
            record.state_id = record.rel_user_id.vat

    @api.depends('rel_user_id')
    def _compute_country_id(self):
        for record in self:
            record.country_id = record.rel_user_id.country_id
