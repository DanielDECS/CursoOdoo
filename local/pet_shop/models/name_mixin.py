from odoo import models, fields

class NameMixin(models.AbstractModel):
    _name = "name.mixin"
    _description = "Name Mixin"

    name = fields.Char(string="Name", required=True)

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'The name of the pet must be unique!'),
    ]