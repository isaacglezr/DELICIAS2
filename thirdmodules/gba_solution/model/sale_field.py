from odoo import api, models, fields

class Sale_field(models.Model):

    _inherit = 'sale.order'

    x_Empleado = fields.Many2one('hr.employee', string="Enfermera")
