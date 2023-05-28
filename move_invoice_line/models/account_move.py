from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', index=True)
    order_id = fields.Many2one('sale.order', string='Sale Order', index=True)
    route_id = fields.Many2one('sale.order.line', string='Route', index=True, domain=[("order_id", "=", order_id.ids)])
    container_num = fields.Char(require=False, string='CONTAINER NUMBER')
    file_name = fields.Char(require=False, string='File Name')
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account')
    size = fields.Char(require=False, string='SIZE')
    weight = fields.Char(require=False, string='WEIGHT')
    consignee = fields.Char(require=False, string='CONSIGNEE')
    srn = fields.Char(require=False, string='SHIPMENT REFERENCE NUMBER')
