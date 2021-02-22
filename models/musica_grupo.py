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
    disco_id = fields.One2many('musica.disco', 'grupo_id', string="Disco", readOnly=True)
    artista_id = fields.One2many('musica.artista', 'grupo_id', string="Artistas", readOnly=True)
    puntuacion = fields.Float(string='Puntuación', compute='_calcular_media')
    anyo = fields.Integer(default=1900, string="Año de fundación");

    # Relational fields:
    pais_id = fields.Many2one('res.country', string="País del grupo")

    # Other fields:
    enactivo = fields.Selection([('activo', 'Activo'), ('disuelto', 'Disuelto')])

    @api.depends('disco_id')
    def _calcular_media(self):
        total = 0
        cont = 0
        for rec in self.disco_id:
            total = total + rec.puntuacion
            cont = cont + 1
        self.puntuacion = total / cont;
