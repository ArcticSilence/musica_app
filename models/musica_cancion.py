from odoo import fields, models


class Cancion(models.Model):
    # Ignacio Sanz
    _name = 'musica.cancion'
    _description = 'Cancion'

    # String fields:
    titulo = fields.Char(
        'Titulo',
        default=None,
        index=True,
        help='Título de la cancion',
        readonly=False,
        required=True,
        translate=False,
    )

    # Numeric fields:
    codigo = fields.Integer
    duracion = fields.Float()

    # Relational fields:
    grupo_id = fields.Many2one('musica.artista', string='Artista')

