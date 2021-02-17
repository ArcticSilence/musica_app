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
    # puntuacion = fields.Float(string='Puntuación', compute='_calcular_media')
    anyo = fields.Integer(default=1900, string="Año de fundación");

    # Relational fields:
    pais_id = fields.Many2one('res.country', string="País del grupo")

    # Other fields:
    enActivo = fields.Boolean('En activo?', default=True)

    @api.depends('disco_id.puntuacion')
    def _calcular_media(self):
        total = 0
        recordset = self.env['musica.disco'].search([])
        for rec in recordset:
            if rec.grupo_id == self.id:
                total += rec.puntuacion
        total = total / recordset.size
