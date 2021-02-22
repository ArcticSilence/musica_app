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

    nombre = fields.Char(
        'Nombre',
        default=None,
        index=True,
        help='Nombre del artista',
        readonly=False,
        required=True,
        translate=False,
    )

    rol = fields.Char(
        'Rol',
        index=True,
        help='Papel en el grupo',
        readonly=False,
        translate=False,
    )

    # Relational fields:
    grupo_id = fields.Many2one('musica.grupo', string='Grupo')

