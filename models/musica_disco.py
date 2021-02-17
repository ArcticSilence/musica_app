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

    # Other fields:
    imagen_disco = fields.Image();

    @api.constrains('puntuacion')
    def _check_value(self):
        if self.puntuacion > 10 or self.puntuacion < 1:
            raise ValidationError('La puntuación debe estar entre 1-10.')

    def _check_EAN(self):
        """Check one Disco's ISBN"""
        self.ensure_one()
        digits = [int(x) for x in self.ean if x.isdigit()]
        if len(digits) == 13:
            ponderators = [1, 3] * 6
            total = sum(a * b for a, b in zip(digits[:12], ponderators))
            remain = total % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_ean(self):
        for disco in self:
            if not disco.ean:
                raise Warning('Please provide an EAN13 for %s' % disco.name)
            if disco.ean and not disco._check_ean:
                raise Warning('%s is an invalid ISBN' % disco.ean)
        return True
