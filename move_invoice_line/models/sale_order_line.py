# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = "Sales Order Line"

    container_num = fields.Char(required=False, string='CONTAINER NUMBER')
    file_name = fields.Char(required=False, string='File Name')
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', required=False, index=True)
    srn = fields.Char(required=False, string='SHIPMENT REFERENCE NUMBER')
    consignee = fields.Char(required=False, string='CONSIGNEE')
    size = fields.Char(required=False, string='SIZE')
    weight = fields.Char(required=False, string='WEIGHT')

    def _prepare_invoice_line(self, **optional_values):
        """
       add vehicle_id value to invoice line
        """
        values = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        values.update({'vehicle_id': self.vehicle_id, 'container_num': self.container_num, 'consignee': self.consignee})
        return values
