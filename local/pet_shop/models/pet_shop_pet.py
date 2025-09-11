from odoo import models, fields, api   
from odoo.exceptions import ValidationError

class PetShopPet(models.Model):
    _name = "pet_shop.pet"
    _description = "Pet"

    name = fields.Char(string="Name", required=True)

    bio = fields.Text(string="Bio", help= "A short description of the pet")

    sex = fields.Selection(string = "Sex", selection=[
        ("male", "Male"),
        ("female", "Female"),
    ])

    birth_certificate = fields.Binary(string="Birth Certificate", attachment=True)

    photo = fields.Image(string="Photo")

    adopted = fields.Boolean(string="Adopted",
                            default=False,
                            help="Whether the pet has been adopted or not",
                            )

    birth_date = fields.Date(string="Birth Date")

    age = fields.Integer(string="Age" , readonly=True, compute="_compute_age")

    weight = fields.Float(string="Weight (kg)", digits=(12, 2))

    owner_id = fields.Many2one(
        string="Owner", 
        comodel_name="res.partner", 
        ondelete="set null",
        )

    vaccine_ids = fields.One2many(
        string="Vaccines", 
        comodel_name="pet_shop.vaccine",
        inverse_name="pet_id",
        )
    
    course_ids = fields.Many2many(
        string="Courses",
        comodel_name="pet_shop.course",
        relation="pet_shop_pet_course_rel",
        column1="pet_id",
        column2="course_id",
        )
    
    currency_id = fields.Many2one(string="Currency", comodel_name="res.currency", required=True)
    
    price = fields.Monetary(string="Price", currency_field="currency_id")

    owner_name = fields.Char(string="Owner Name", related="owner_id.name", store=True)

    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            if record.birth_date and record.birth_date > fields.Date.today():
                raise ValidationError("The birth date cannot be in the future!")

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                delta = fields.Date.today() - record.birth_date
                record.age = delta.days // 365
            else:
                record.age = 0
   
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'The name of the pet must be unique!'),
        ('positive_weight', 'CHECK(weight > 0)', 'The weight must be positive!'),
]