from odoo import models, fields

class ResPartner(models.Model):
    _name = "res.partner.owner"
    _inherits = {"res.partner": "partner_id"}
    # _inherit = "res.partner"

    partner_id = fields.Many2one(
        comodel_name="res.partner", 
        ondelete="cascade",
        required=True
    )
    favorite_pet_type_id = fields.Many2one(
        comodel_name="pet_shop.pet.type", 
        string="Favorite Pet Type",
        ondelete="set null",
    )

    
    # channel_ids = fields.Many2many(
    #     "mail.channel",
    #     "mail_channel_partner_owner",
    #     "partner_id",
    #     "channel_id",
    #     string="Channels",
    #     copy=False
    # )
    