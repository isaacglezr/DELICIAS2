# -*- coding: utf-8 -*-
{
    'name': 'Pacientes Delicias',
    'summary': """
         Para la mejor administracion y asignacion de habitaciones y salas""",

    'description': """
        Este modulo permitira una mejor gestion de pacientes en la clinica, asi como los materiales a utilizar """,

    'author': "GBA Tecnologías",
    'website': "http://www.gba.com.mx",

    'category': 'service',
    'version': '0.1',

    'depends': ['base', 'contacts', 'stock', 'medicos'],

    'data': [
        'view/pacientes_view.xml',
        'view/partner_fields_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
