from odoo import models, fields, api

class Ingredientes(models.Model):
    _name = 'charcuteria.ingredientes'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio', required=True)
    cantidad = fields.Float('Cantidad', required=True)
    perecedero = fields.Boolean('Perecedero', required=True)
    proveedores = fields.Many2one('charcuteria.proveedores', 'Proveedores')

    @api.one
    def aniadir(self):
        self.cantidad = self.cantidad + 1
