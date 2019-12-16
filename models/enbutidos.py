from odoo import models, fields

class Panes(models.Model):
    _name = 'charcuteria.embutidos'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio', required=True)
    temporada = fields.Char('Temporada', required=False)
    
