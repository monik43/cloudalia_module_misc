# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class respartner(models.Model):
    _inherit = 'res.partner'

    escola_associada = fields.Many2One(compute="_get_escola_from_user")

    @api.depends('payment_responsible_id')
    def _get_escola_from_user(self):
        user = self.env['res.users'].search([('id','=',self.payment_responsible_id)])
        if user.escola == 'cmontserrat_c':
            self.escola_associada = self.env['res.partner'].search([('id','=','16923')])


    ##TODO: adaptar metodo
    @api.model
    def signup_retrieve_info_escola(self, token):
        """ retrieve the user info about the token
            :return: a dictionary with the user information:
                - 'db': the name of the database
                - 'token': the token, if token is valid
                - 'name': the name of the partner, if token is valid
                - 'login': the user login, if the user already exists
                - 'email': the partner email, if the user does not exist
        """
        partner = self._signup_retrieve_partner(token, raise_exception=True)
        res = {'db': self.env.cr.dbname}
        if partner.signup_valid:
            res['token'] = token
            res['name'] = partner.name
        if partner.user_ids:
            res['login'] = partner.user_ids[0].login
        else:
            res['email'] = res['login'] = partner.email or ''
        return res