from odoo import models, fields

class PetShopPetType(models.Model):
    _name = "pet_shop.pet.type"
    _description = "Pet Type"

    name = fields.Char(string="Name", required=True)

    description = fields.Text(string="Description")