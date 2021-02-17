from odoo import fields, models, api

from odoo.exceptions import Warning


class Club(models.Model):
    _name = 'musica.club'
    _description = 'Club'
    cod = fields.Integer('Codigo', required=True)
    name = fields.Char('Nombre')
    sede = fields.Char('Sede', default=True)
    num = fields.Integer('Numero')
    active = fields.Boolean('Active?', default=True)
    cod_group = fields.Many2one('res.partner', string='Grupo')
