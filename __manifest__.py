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

    'version': '11.0.0.7',

    'depends': ['base', 'auth_signup', 'website', 'account'],

    'data': [
        'views/auth_signup_views.xml',
        'views/auth_signup_assets.xml'
    ],
    'installable': True,
    'auto_install': True,
}