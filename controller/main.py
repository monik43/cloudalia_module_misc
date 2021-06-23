# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import logging
import werkzeug
from werkzeug import routing
from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.exceptions import UserError
from odoo.http import request

_logger = logging.getLogger(__name__)


class AuthSignupHome(AuthSignupHome):

    @http.route(['/web/signup', '/web/signup?es=<int:es>'], type='http', auth='public', website=True,
                sitemap=False, methods=['GET', 'POST'])
    def web_auth_signup(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()
        value_dict = dict(kw)
        print(bool(value_dict))
        print(value_dict)
        print(bool(dict(kw)))
        print(dict(kw))
        print(bool(kw))
        print(kw)
        if bool(value_dict["es"]):
            escoles = {'holi': 1, 'cmontserrat': 2,
                       'eminguella': 3, 'jpelegri': 4, 'lestonnac': 5, 'inscassaselva': 6, 'stesteve': 7, 'bitacola': 8}
            
            for school in escoles:
                if str(value_dict["es"]).find(str(escoles[school])) != -1:
                    escola = escoles[school]
            qcontext = self.get_auth_signup_qcontext()
            qcontext['states'] = request.env['res.country.state'].sudo().search([
            ])
            qcontext['countries'] = request.env['res.country'].sudo().search([])

            if not qcontext.get('token') and not qcontext.get('signup_enabled'):
                raise werkzeug.exceptions.NotFound()
            if 'error' not in qcontext and request.httprequest.method == 'POST':
                try:
                    self.do_signup(qcontext, escola)
                    # Send an account creation confirmation email
                    if qcontext.get('token'):
                        user_sudo = request.env['res.users'].sudo().search(
                            [('login', '=', qcontext.get('login'))])
                        template = request.env.ref(
                            'auth_signup.mail_template_user_signup_account_created',
                            raise_if_not_found=False)
                        if user_sudo and template:
                            template.sudo().with_context(
                                lang=user_sudo.lang,
                                auth_login=werkzeug.url_encode({
                                    'auth_login': user_sudo.email
                                }),
                            ).send_mail(user_sudo.id, force_send=True)
                    return super(AuthSignupHome, self).web_login(*args, **kw)
                except UserError as e:
                    qcontext['error'] = e.name or e.value
                except (SignupError, AssertionError) as e:
                    if request.env["res.users"].sudo().search(
                            [("login", "=", qcontext.get("login"))]):
                        qcontext["error"] = _(
                            "Another user is already registered using this email address.")
                    else:
                        _logger.error("%s", e)
                        qcontext['error'] = _(
                            "Could not create a new account.")
            response = request.render(
                'cloudalia_module_misc.registro_login', qcontext)
        else:
            qcontext = self.get_auth_signup_qcontext()
            qcontext['states'] = request.env['res.country.state'].sudo().search([
            ])
            qcontext['countries'] = request.env['res.country'].sudo().search([])

            if not qcontext.get('token') and not qcontext.get('signup_enabled'):
                raise werkzeug.exceptions.NotFound()

            if 'error' not in qcontext and request.httprequest.method == 'POST':
                try:
                    self.do_signup(qcontext)
                    # Send an account creation confirmation email
                    if qcontext.get('token'):
                        user_sudo = request.env['res.users'].sudo().search(
                            [('login', '=', qcontext.get('login'))])
                        template = request.env.ref(
                            'auth_signup.mail_template_user_signup_account_created',
                            raise_if_not_found=False)
                        if user_sudo and template:
                            template.sudo().with_context(
                                lang=user_sudo.lang,
                                auth_login=werkzeug.url_encode({
                                    'auth_login': user_sudo.email
                                }),
                            ).send_mail(user_sudo.id, force_send=True)
                    return super(AuthSignupHome, self).web_login(*args, **kw)
                except UserError as e:
                    qcontext['error'] = e.name or e.value
                except (SignupError, AssertionError) as e:
                    if request.env["res.users"].sudo().search(
                            [("login", "=", qcontext.get("login"))]):
                        qcontext["error"] = _(
                            "Another user is already registered using this email address.")
                    else:
                        _logger.error("%s", e)
                        qcontext['error'] = _(
                            "Could not create a new account.")

            response = request.render('auth_signup.signup', qcontext)

        response.headers['X-Frame-Options'] = 'DENY'
        return response

    def do_signup(self, qcontext, *kw):
        """ Shared helper that creates a res.partner out of a token """
        if qcontext.get('mobile'):
            values = {key: qcontext.get(key)
                      for key in ('login', 'name', 'password', 'mobile', 'vat', 'street', 'street2', 'zip', 'city', 'state_id', 'country_id', 'escola')}
            
            values.update({'escola': kw[0]})
            if not values:
                raise UserError(_("The form was not properly filled in."))
            if values.get('password') != qcontext.get('confirm_password'):
                raise UserError(
                    _("Passwords do not match; please retype them."))
            supported_langs = [
                lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
            if request.lang in supported_langs:
                values['lang'] = request.lang
            self._signup_with_values(qcontext.get('token'), values)
            request.env.cr.commit()
        else:
            values = {key: qcontext.get(key)
                      for key in ('login', 'name', 'password')}
            if not values:
                raise UserError(_("The form was not properly filled in."))
            if values.get('password') != qcontext.get('confirm_password'):
                raise UserError(
                    _("Passwords do not match; please retype them."))
            supported_langs = [
                lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
            if request.lang in supported_langs:
                values['lang'] = request.lang
            self._signup_with_values(qcontext.get('token'), values)
            request.env.cr.commit()
