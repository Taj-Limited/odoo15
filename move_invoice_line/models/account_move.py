from odoo import api, models

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', index=True)
    order_id = fields.Many2one('sale.order', string='Sale Order', index=True)
    route_id = fields.Many2one('sale.order.line', string='Route', index=True)