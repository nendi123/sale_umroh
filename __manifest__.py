# -*- coding: utf-8 -*-
{
    'name': "Sale Umroh",

    'summary': """
        Module Base Common Config""",

    'description': """
        Manajemen Common Model
    """,

    'author': "Nendi Isharmawan",
    'website': "",

    'category': 'Sales',
    'version': '0.1',

		# Depencicy
    'depends': ['base','mail','sale'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        'views/sale.order.views.xml',
        'views/res.partner.views.xml',
        'report/report_invoice_document_inherit.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}