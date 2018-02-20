from odoo import api, fields, models

class Medicos(models.Model):

    _name="medico.delicias"

    name = fields.Char(string="Nombre")
    x_Especialidad = fields.Char(string="Especialidad")
    x_movil = fields.Char(string="Telefono")
