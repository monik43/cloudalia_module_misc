# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import float_is_zero



class respartner(models.Model):
    _inherit = 'res.partner'

    
    escola = fields.Char()


    credit_limit = fields.Float(string='Credit Limit', compute="_compute_credit")
    escola_id = fields.Char(string="Escola", compute="_compute_escola")
    #mobile = fields.Char(compute="_compute_mobile")
    #street = fields.Char(compute="_compute_street")
    #street2 = fields.Char(compute="_compute_street2")
    #zip = fields.Char(change_default=True, compute="_compute_zip")
    #city = fields.Char(compute="_compute_city")
    #state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', compute="_compute_state_id")
    #vat = fields.Char(string='TIN', help="Tax Identification Number. Fill it if the company is subjected to taxes. Used by the some of the legal statements.", compute="_compute_vat")

    @api.multi
    def print_nfo(self):
        for record in self:

            print(record.escola_id)


    def _compute_credit(self):
        for record in self:
            if record.escola_id != False and float_is_zero(record.credit_limit, precision_digits=2):
                record.credit_limit = 600.0

    def _compute_escola(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False:
                record.escola_id = rel_user.escola

                with switch(record.escola_id) as e:
                    if e.case('2',True):  # cmontserrat
                        record.write({'product_ids': [(6, 0, [3660, 3661])]})
                    if e.case('3',True):  # eminguella
                        record.write({'product_ids': [(6, 0, [3664])]})
                    if e.case('4',True):  # jpelegri
                        record.write({'product_ids': [(6, 0, [3665])]})
                    if e.case('5',True):  # lestonnac
                        record.write({'product_ids': [(6, 0, [3671])]})
                    if e.case('6',True):  # inscassaselva
                        record.write({'product_ids': [(6, 0, [3676, 3677])]})
                    if e.case('7',True):  # stesteve
                        record.write({'product_ids': [(6, 0, [3683])]})
                    if e.case('8',True):  # bitacola
                        record.write({'product_ids': [(6, 0, [3684])]})
                    if e.case('9',True):  # gresol
                        record.write({'product_ids': [(6, 0, [3695, 3696])]})
                    if e.case('10',True):  # fcambo
                        record.write({'product_ids': [(6, 0, [3695, 3696])]})

    def _compute_mobile(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False and rel_user.mobile != False:
                record.mobile = rel_user.mobile

    def _compute_street(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False and rel_user.street != False:
                record.street = rel_user.street

    def _compute_street2(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False and rel_user.street2 != False:
                record.street2 = rel_user.street2

    def _compute_zip(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False and rel_user.zip != False:
                record.zip = rel_user.zip

    def _compute_city(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False and rel_user.city != False:
                record.city = rel_user.city

    def _compute_state_id(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False and rel_user.state_id != False:
                record.state_id = rel_user.state_id
                record.country_id = rel_user.state_id.country_id

    def _compute_vat(self):
        for record in self:
            rel_user = record.env['res.users'].search([('partner_id', '=', record.id)])
            if rel_user and rel_user.escola != False and rel_user.vat != False:
                record.vat = rel_user.vat


class switch:

	def __init__(self, variable, comparator=None, strict=False):
		self.variable = variable
		self.matched = False
		self.matching = False
		if comparator:
			self.comparator = comparator
		else:
			self.comparator = lambda x, y: x == y
		self.strict = strict

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		pass

	def case(self, expr, break_=False):
		if self.strict:
			if self.matched:
				return False
		if self.matching or self.comparator(self.variable, expr):
			if not break_:
				self.matching = True
			else:
				self.matched = True
				self.matching = False
			return True
		else:
			return False

	def default(self):
		return not self.matched and not self.matching