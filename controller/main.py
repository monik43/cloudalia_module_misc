# -*- coding: utf-8 -*-

import logging
import werkzeug
from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.exceptions import UserError
from odoo.http import request

_logger = logging.getLogger(__name__)


class AuthSignupHome(AuthSignupHome):

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        if qcontext.get('escola'):
            print("escola si ", qcontext.get('escola'))
            values = {key: qcontext.get(key)
                for key in ('login', 'name', 'password','escola')}
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
            print("escola no")
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

    @http.route('/web/signup', type='http', auth='public', website=True,
                sitemap=False)
    def web_auth_signup(self, *args, **kw):

        last_url = request.httprequest.environ['HTTP_REFERER']
        url_escola = False
        escoles = {'holi', 'cmontserrat'}

        for escola in escoles:
            if last_url.find(escola) != -1:
                print("holi es el url anterior")
                url_escola = True
                print(url_escola)

        if url_escola:
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

    def get_auth_signup_qcontext(self):
        """ Shared helper returning the rendering context for signup and reset password """
        qcontext = request.params.copy()
        print(request.params)
        qcontext.update(self.get_auth_signup_config())
        if not qcontext.get('token') and request.session.get('auth_signup_token'):
            qcontext['token'] = request.session.get('auth_signup_token')
        if qcontext.get('token'):
            try:
                # retrieve the user info (name, login or email) corresponding to a signup token
                token_infos = request.env['res.partner'].sudo(
                ).signup_retrieve_info(qcontext.get('token'))
                for k, v in token_infos.items():
                    qcontext.setdefault(k, v)
            except:
                qcontext['error'] = _("Invalid signup token")
                qcontext['invalid_token'] = True
        return qcontext
