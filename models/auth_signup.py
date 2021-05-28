# -*- coding: utf-8 -*-
from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class authsignupescola(AuthSignupHome):
    def _signup_with_values(self, token, values):
        context = self.get_auth_signup_qcontext()
        values.update({'escola': context.get('escola')})
        super(authsignupescola, self)._signup_with_values(token, values)