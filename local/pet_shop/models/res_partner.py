from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    favorite_pet_type_id = fields.Many2one(
        comodel_name="pet_shop.pet.type", 
        string="Favorite Pet Type",
        ondelete="set null",
    )
    