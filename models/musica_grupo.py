from odoo import fields, models


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
    pais = fields.Char('País')
