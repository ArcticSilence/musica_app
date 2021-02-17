from odoo import fields, models, api

from odoo.exceptions import Warning


class Club(models.Model):
    # Guillermo Bort
    _name = 'musica.club'
    _description = 'Club'
    cod = fields.Integer('Codigo', required=True)
    name = fields.Char('Nombre')
    sede = fields.Char('Sede')
    num = fields.Integer('Numero')
    active = fields.Boolean('Active?', default=True)
    cod_group = fields.Many2one('musica.grupo', string='Grupo')
