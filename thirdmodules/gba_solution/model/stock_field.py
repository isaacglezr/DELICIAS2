from odoo import api, fields, models

class Stock_field(models.Model):

    _inherit = 'stock.picking'

    x_Empleado = fields.Many2one('hr.employee', string="Enfermera", readonly=True, compute="_orden_agregar")

    @api.multi
    @api.depends('origin')
    def _orden_agregar(self):
        for record in self:
            if self.origin != "":
                record['x_Empleado'] = self.env['sale.order'].search([('name', '=', self.origin)]).x_Empleado
