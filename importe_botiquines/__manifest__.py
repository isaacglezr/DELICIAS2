# -*- coding: utf-8 -*-
{
    'name': "Importe_Botiquin",

    'summary': """Suma de Subtotal por Categoria Interna""",

    'description': """
   
    """,

    'author': "GBA Tecnologias",
    'website': "http://www.gba.com.mx",

    'category': 'invoice',
    'version': '0.1',

    'depends': ['base', 'account'],

    'data': [
        'view/botiquin_view.xml'
        #'templates.xml',
    ],
    'demo': [
        #'demo.xml',
    ],
    'installable': True,
    'auto_install': False,  
}