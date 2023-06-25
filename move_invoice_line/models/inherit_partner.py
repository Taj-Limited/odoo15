from odoo import models, api, fields


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    vrn = fields.Char(string='VRN NO',  store=True, require=False)
