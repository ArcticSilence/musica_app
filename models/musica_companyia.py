from odoo import fields, models, api

from odoo.exceptions import Warning


class Companyia(models.Model):
    _name = 'musica.companyia'
    _description = 'Companyia'
    cod = fields.Integer('Codigo', required=True)
    name = fields.Char('Nombre')
    dir = fields.Char('direccion')
    fax = fields.Char('Fax')
    tlfn = fields.Char('Telefono')
    active = fields.Boolean('Active?', default=True)
