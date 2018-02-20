from odoo import api, fields, models

class Habitacion(models.Model):

    _name='num.habitacion'

    name=fields.Char(string='Numero de Habitacion')
    x_Disponible = fields.Boolean(string='Ocupada')

#    @api.one
 #   def _set_ocupada(self):
  #      if(self._cr.execute("SELECT id FROM pacientes.delicias where x_Habitacion="+str(x_numhab)+";")):
   #         self.x_Disponible=True
