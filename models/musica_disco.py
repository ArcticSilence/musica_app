from odoo import fields, models


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

    # Relational fields:
    grupo = fields.One2one()
    companyia = fields.One2many()

    def _check_ean(self):
        """Check one Book's ISBN"""
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderators = [1, 3] * 6
            total = sum(a * b for a, b in zip(digits[:12], ponderators))
            remain = total % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    def button_check_isbn(self):
        for disco in self:
            if not disco.ean:
                raise Warning('Please provide an ISBN13 for %s' % book.name)
            if disco.ean and not disco._check_ean:
                raise Warning('%s is an invalid ISBN' % book.isbn)
        return True
