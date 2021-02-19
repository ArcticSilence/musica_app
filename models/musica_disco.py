from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Disco(models.Model):
    # Álvaro Sobrino
    _name = 'musica.disco'
    _description = 'Disco'

    # String fields:
    name = fields.Char(
        'Titulo',
        default=None,
        index=True,
        help='Título del disco',
        readonly=False,
        required=True,
        translate=False,
    )
    ean = fields.Char("EAN")

    # Date fields:
    fecha_publicacion = fields.Date()
    genero = fields.Selection(
        [('rock', 'Rock'), ('metal', 'Metal'), ('electronica', 'Electrónica'), ('reggae', 'Reggae')])

    # Numeric fields:
    copias = fields.Integer(default=1)
    puntuacion = fields.Float(default=5)

    # Relational fields:
    grupo_id = fields.Many2one('musica.grupo', string='Grupo')
    comp_id = fields.Many2one('musica.companyia', string='Compañía')
    cancion_id = fields.Many2one('musica.cancion', string='Canciones')

    # Other fields:
    imagen_disco = fields.Image();

    @api.constrains('puntuacion')
    def _check_value(self):
        if self.puntuacion > 10 or self.puntuacion < 1:
            raise ValidationError('La puntuación debe estar entre 1-10.')

    @api.constrains('grupo_id')
    def _check_grupo(self):
        if not self.grupo_id:
            raise ValidationError('El grupo no puede estar vacío.')
