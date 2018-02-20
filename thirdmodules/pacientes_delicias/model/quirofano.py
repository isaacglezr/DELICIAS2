from odoo import api, fields, models

class Quirofano(models.Model):

    _name='num.quirofano'

    name = fields.Char(string='Sala de Quirofano')
    x_disponible = fields.Boolean(string='Ocupada')
