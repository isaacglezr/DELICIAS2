# -*- coding: utf-8 -*-
{
    'name': "stock_field",

    'summary': """
        aditional fields to stock_picking
    """,

    'description': """
        New Module to add new fields to stock_picking form
    """,

    'author': "GBA Tecnologias",
    'website': "http://www.gba.com.mx",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale_management'],

    # always loaded
    'data': [
        'view/stock_field_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
