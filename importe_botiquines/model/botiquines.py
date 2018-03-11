# -*- coding: utf-8 -*-
from odoo import models, fields, api

    class Botiquines(models.Model):
    
    _inherit='account.invoice'
    
    x_botiquin=fields.Monetary(string="Botiquin", readonly=True)
    x_material=fields.Monetary(string="Material", readonly=True)
    x_servicio=fields.Monetary(string="Servicio", readonly=True)
    
    def _get_subtotal_categ(self):
        for record in self:
            record['x_botiquin']= sum(line.price_subtotal for line in self.invoice_line_ids)
            record['x_material']= sum(line.price_subtotal for line in self.invoice_line_ids)
            record['x_servicio']= sum(line.price_subtotal for line in self.invoice_line_ids)
    
    
    
    
    
    #for record in self:
  #record['x_botiquin'] = sum(line.price_subtotal for line in self.invoice_line_ids)