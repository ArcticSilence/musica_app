from odoo import fields, models


class Cancion(models.Model):
    # Ignacio Sanz
    _name = 'musica.cancion'
    _description = 'Cancion'

    # String fields:
    name = fields.Char(
        'Titulo',
        default=None,
        index=True,
        help='Título de la cancion',
        readonly=False,
        required=True,
        translate=False,
    )

    # Numeric fields:
    cod = fields.Integer
    duracion = fields.Float((15, 5))

    # Relational fields:
    grupo_id = fields.Many2one('musica.artista', string='Artista')

