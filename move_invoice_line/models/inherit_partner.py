from odoo import models, api, fields


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    vrn = fields.Text(string='VRN NO',  store=True, readonly=True)
