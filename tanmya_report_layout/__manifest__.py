# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'ALTANMYA Report Layout',
    'version': '1.0',
    'category': 'Web/Reporting',
    'summary': 'Define a custom report layout',
    'depends': ['web', 'web_studio'],
    'author': 'ALTANMYA - TECHNOLOGY SOLUTIONS',
    'company': 'ALTANMYA - TECHNOLOGY SOLUTIONS Part of ALTANMYA GROUP',
    'website': "http://tech.altanmya.net",
    'data': [
         'views/tanmya_layout.xml',
    ],
    'assets': {
        'web_studio.studio_assets': [
            'tanmya_report_layout/static/src/js/tanmya_layout.js'
        ]
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
