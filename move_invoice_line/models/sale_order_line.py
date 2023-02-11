# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = "Sales Order Line"

    container_num = fields.Char(require=False, string='CONTAINER NUMBER')
    file_name = fields.Char(require=False, string='File Name')
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', require=False, index=True)
