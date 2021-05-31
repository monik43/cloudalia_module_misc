from odoo.addons.auth_oauth.controllers.main import OAuthLogin
import functools
import logging

import json

import werkzeug.urls
import werkzeug.utils
from werkzeug.exceptions import BadRequest

from odoo import api, http, SUPERUSER_ID, _
from odoo.exceptions import AccessDenied
from odoo.http import request
from odoo import registry as registry_get

from odoo.addons.cloudalia_module_misc.controllers.auth_signup import authsignuphome_escola as Home
from odoo.addons.web.controllers.main import db_monodb, ensure_db, set_cookie_and_redirect, login_and_redirect


_logger = logging.getLogger(__name__)

class oauthlogin_escola(OAuthLogin):

    @http.route()
    def web_auth_signup_escola(self, *args, **kw):
        providers = self.list_providers()
        response = super(OAuthLogin, self).web_auth_signup_escola(*args, **kw)
        response.qcontext.update(providers=providers)
        return response
