# -*- coding: utf-8 -*-
{
    'name': "cloudalia_module_misc",

    'summary': """
        Modulo Cloudalia.""",

    'description': """Cloudalia Educación odoo module.
    """,

    'author': "Cloudalia Educacion",

    'website': "http://www.cloudaliaeducacion.com",

    'category': 'Technical Settings',

    'version': '11.0.0.1',

    'depends': ['base', 'stock', 'cloudedu_mods', 'auth_signup', 'website'],

    'data': [
        'views/auth_signup_views.xml',
        'views/res_partner_views.xml',
        #'views/stock_views.xml',
        #'views/views.xml',
    ],
}