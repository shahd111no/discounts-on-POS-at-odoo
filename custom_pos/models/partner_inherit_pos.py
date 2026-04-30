from odoo import api, fields, models

class PartnerInheritPos(models.Model):
    _inherit = "res.partner"

    discount=fields.Float(default=0.0)