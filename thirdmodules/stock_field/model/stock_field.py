from odoo import api, fields, models

class Sale_fields(models.Model):

    _inherit='stock.picking'

    x_Cotiza = fields.Many2one('sale.order', string="Cotizacion/Venta")

    @api.onchange('x_Cotiza')
    def _onchange_product(self):
        if self.x_Cotiza:
            self.partner_id = self.x_Cotiza.partner_id
            #self.move_lines = self.env['sale.order'].search([('name','=',self.x_Cotiza.name)]).order_line
            self.move_lines.product_id.name = self.x_Cotiza.order_line.product_id.name
