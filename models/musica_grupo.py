from odoo import fields, models, api


class Grupo(models.Model):
    _name = 'musica.grupo'
    _description = 'Grupo'
    _order = 'name'

    # String fields:
    name = fields.Char(
        'Nombre',
        default=None,
        index=True,
        help='Nombre del grupo',
        readonly=False,
        required=True,
        translate=False,
    )

    # Numeric fields:
    disco_id = fields.Many2one('musica.disco', string="Disco")
    puntuacion = fields.Float(string='Puntuación', compute='_calcular_media')
    anyo = fields.Integer(default=1900, string="Año de fundación");

    # Relational fields:
    pais_id = fields.Many2one('res.country', string="País del grupo")

    # Other fields:
    # enactivo = fields.Boolean('¿En activo?', default=True)
    # stringactivo = fields.Char(compute='grupo_en_activo')

    @api.depends('disco_id')
    def _calcular_media(self):
        self.puntuacion = 8
        cont = 0
        for rec in self.disco_id:
            self.puntuacion = self.puntuacion + rec.puntuacion
            cont += 1

    def grupo_en_activo(self):
        if self.enactivo:
            return "En activo"
        else:
            return "Disuelto"
