from odoo import api, fields, models

class New_fields_partner(models.Model):

    _inherit = "res.partner"

    x_NumExpediente = fields.Char(string='Expediente')
    x_medico = fields.Many2one('medico.delicias', string="Doctor")
    x_Privado = fields.Many2one('num.habitacion', string="Privado")
    x_Historial = fields.Many2many('pacientes.delicias', string="Historial Clinico")
    x_Edad = fields.Char(string="Edad")
