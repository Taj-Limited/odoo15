# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Order"

    container_num = fields.Char(require=False, string='CONTAINER NUMBER')
    file_name = fields.Char(require=False, string='File Name')
