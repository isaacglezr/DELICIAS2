from odoo import api, fields, models

class Pacientes_delicias(models.Model):
    _name='pacientes.delicias'
    
    name=fields.Many2one('res.partner', string='Paciente', required=True)
    x_FechaEntrada = fields.Datetime(string='Fecha de Ingreso')
    x_FechaSalida = fields.Datetime(string='Fecha de Alta')
    x_Expediente = fields.Char(string='Expediente')
    x_Doctor = fields.Many2one('medico.delicias', string='Doctor')
    state = fields.Selection([('draft', "Borrador"), ('confirmed', "Abierto"), ('done', "Pagado"),], default='draft', readonly=True)
    x_Diagnostico = fields.Text(string='Diagnostico/Padecimiento')

    #Habitacion
    x_Habitacion = fields.Boolean(string='Requiere Habitacion')
    x_NumHabitacion = fields.Many2one('num.habitacion', string='Numero de Habitacion')
    x_ExistenciaH = fields.Many2many('stock.quant', string='Existencia en Hospital')

    #Quirofano
    x_Quirofano = fields.Boolean(string='Quirofano')
    x_NumQuirofano = fields.Many2one('num.quirofano', string='Sala de Quirofano')
    x_ExistenciaQ = fields.Many2many('stock.quant', string='Existencia en Quirofano')

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'

    @api.multi
    def action_done(self):
        self.state = 'done'

    @api.onchange('name')
    def _onchange_employee_id(self):
        if self.name:
            self.x_Expediente = self.name.x_NumExpediente
