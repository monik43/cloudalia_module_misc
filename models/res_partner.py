# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import float_is_zero
from . import switch


class respartner(models.Model):
    _inherit = 'res.partner'

    centro_educativo = fields.Many2one("res.partner", compute="_compute_centro_educativo")
    escola = fields.Char()
    rel_user_id = fields.Many2one("res.users", compute="_compute_usuari")
    credit_limit = fields.Float(
        string='Credit Limit', compute="_compute_credit")
    productes_ids = fields.Many2many('product.template', 'productes_template_id',
                                     'res_partner_id', 'product_partner_res', string='Productes')

    escola_id = fields.Char(string="Escola", compute="_compute_escola")
    mobile = fields.Char(compute="_compute_mobile")
    street = fields.Char(compute="_compute_street")
    street2 = fields.Char(compute="_compute_street2")
    zip = fields.Char(change_default=True, compute="_compute_zip")
    city = fields.Char(compute="_compute_city")
    state_id = fields.Many2one(
        "res.country.state", string='State', ondelete='restrict', compute="_compute_state_id")
    country_id = fields.Many2one(
        "res.country", string='Country', compute="_compute_country_id", store=True)
    vat = fields.Char(string='TIN', help="Tax Identification Number. "
                                         "Fill it if the company is subjected to taxes. "
                                         "Used by the some of the legal statements.", compute="_compute_vat")

    @api.onchange('id')
    def _compute_usuari(self):
        for record in self:
            if record.env['res.users'].search([('partner_id', '=', record.id)]).escola != False:
                record.rel_user_id = record.env['res.users'].search(
                    [('partner_id', '=', record.id)])

    def _compute_credit(self):
        for record in self:
            if record.escola_id != False and float_is_zero(record.credit_limit, precision_digits=2):
                record.credit_limit = 600.0

    def _compute_escola(self):
        for record in self:
            if record.rel_user_id.escola != False:
                record.escola_id = record.rel_user_id.escola
                
                with switch(record.escola_id) as e:
                    if e.case(2):#cmontserrat
                        record.write({'product_ids': [(6, 0, [3660, 3661])]})
                    if e.case(3):#eminguella
                        record.write({'product_ids': [(6, 0, [3664])]})
                    if e.case(4):#jpelegri
                        record.write({'product_ids': [(6, 0, [3665])]})
                    if e.case(5):#lestonnac
                        record.write({'product_ids': [(6, 0, [3671])]})
                    if e.case(6):#inscassaselva
                        record.write({'product_ids': [(6, 0, [3676, 3677])]})
                    if e.case(7):#stesteve
                        record.write({'product_ids': [(6, 0, [3683])]})
                    if e.case(8):#bitacola
                        record.write({'product_ids': [(6, 0, [3684])]})
                    if e.case(9):#gresol
                        record.write({'product_ids': [(6, 0, [3695,3696])]})
                    if e.case(10):#fcambo
                        record.write({'product_ids': [(6, 0, [3695,3696])]})

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
            record.vat = record.rel_user_id.vat

    def _compute_country_id(self):
        for record in self:
            record.country_id = record.rel_user_id.state_id.country_id

    def _compute_centro_educativo(self):
        for record in self:
            if record.escola_id:
                with switch(record.escola_id) as e:
                    if e.case(2):#cmontserrat
                        record.centro_educativo = record.env['res.partner'].browse(16923)
                    if e.case(3):#eminguella
                        record.centro_educativo = record.env['res.partner'].browse(12794)
                    if e.case(4):#jpelegri
                        record.centro_educativo = record.env['res.partner'].browse(12359)
                    if e.case(5):#lestonnac
                        record.centro_educativo = record.env['res.partner'].browse(9583)
                    if e.case(6):#inscassaselva
                        record.centro_educativo = record.env['res.partner'].browse(19874)
                    if e.case(7):#stesteve
                        record.centro_educativo = record.env['res.partner'].browse(14984)
                    if e.case(8):#bitacola
                        record.centro_educativo = record.env['res.partner'].browse(9737)
                    if e.case(9):#gresol
                        record.centro_educativo = record.env['res.partner'].browse(13114)
                    if e.case(10):#fcambo
                        record.centro_educativo = record.env['res.partner'].browse(9839)
            


