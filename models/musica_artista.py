from odoo import fields, models


class Artista(models.Model):
    # Ignacio Sanz
    _name = 'musica.artista'
    _description = 'Artista'

    # String fields:
    dni = fields.Char(
        'dni',
        default=None,
        index=True,
        help='DNI del artista',
        readonly=False,
        required=True,
        translate=False,
    )

    name = fields.Char(
        'Nombre',
        default=None,
        index=True,
        help='Nombre dek artista',
        readonly=False,
        required=True,
        translate=False,
    )

    # Relational fields:
    grupo_id = fields.Many2one('musica.grupo', string='Grupo')

