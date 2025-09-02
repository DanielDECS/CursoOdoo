from odoo import models, fields


class PetShopPet(models.Model):
    _name = "pet_shop.pet"
    _description = "Pet"

    name = fields.Char(string="Name")

    bio = fields.Text(string="Bio", help= "A short description of the pet")

    sex = fields.Selection(string = "Sex", selection=[
        ("male", "Male"),
        ("female", "Female"),
    ])

    birth_certificate = fields.Binary(string="Birth Certificate", attachment=True)

    photo = fields.Image(string="Photo")

    adopted = fields.Boolean(string="Adopted", default=False, help="Whether the pet has been adopted or not")

    birth_date = fields.Date(string="Birth Date")

    age = fields.Integer(string="Age")

    weight = fields.Float(string="Weight (kg)", digits=(12, 2))

    




