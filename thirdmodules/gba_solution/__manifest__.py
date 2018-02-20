# -*- coding: utf-8 -*-
{
    'name': "gba_solution",

    'summary': """
        aditional fields to stock_picking - sale_order
    """,

    'description': """
        New Module to add new fields to stock_picking - sale_order form
    """,

    'author': "GBA Tecnologias",
    'website': "http://www.gba.com.mx",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'stock-sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale_management', 'hr'],

    # always loaded
    'data': [
        'view/sale_field_view.xml',
        'view/stock_field_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
