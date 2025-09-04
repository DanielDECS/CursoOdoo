from odoo import models, fields

class PetShopVaccine(models.Model):
    _name = "pet_shop.vaccine"
    _description = "Vaccine for pet"

    name = fields.Char(string="Name" , required=True)

    vaccination_date = fields.Date(string="Vaccination Date")

    pet_id = fields.Many2one(string="Pet", comodel_name="pet_shop.pet", ondelete="cascade")

    

    