from odoo import models, fields

class PetShopPetCourse(models.Model):
    _name = "pet_shop.course"
    _description = "Training Pet Course"
    _inherit = ["name.mixin"]

    # name = fields.Char(string="Name", required=True)

    start_date = fields.Date(string="Start Date")

    end_date = fields.Date(string="End Date")

    currency_id = fields.Many2one(string="Currency", comodel_name="res.currency", required=True)
    
    price = fields.Monetary(string="Price", currency_field="currency_id")