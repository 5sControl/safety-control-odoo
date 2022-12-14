# -*- coding: utf-8 -*-
{
    'name': "Safety Control",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "5sControl",
    'website': "https://eigsoft.com/5scontrol",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/safety_control_menu.xml'
    ],
    'application': True,
    'license': 'LGPL-3'
}