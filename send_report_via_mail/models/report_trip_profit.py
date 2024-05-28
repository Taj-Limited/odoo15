import datetime

from odoo import models, fields


class ReportTripProfit(models.Model):
    _name = 'report.trip.profit'
    _description = "Report Trip Profit"

    order_id = fields.Many2one('sale.order', 'Order')
    truck = fields.Char("Truck")
    root = fields.Many2one('product.template', 'Root')
    trip = fields.Char("Trip")
    size = fields.Char("Size")
    date = fields.Date("Year")
    operating_income = fields.Float("Operating Income")
    total_going = fields.Float("Total Going")
    total_return = fields.Float("Total Return")
    total_fuel = fields.Float("Total Fuel")
    total_cost = fields.Float("Total Cost")
    expenses = fields.Float("Expenses")
    cross_profit = fields.Float('Cross Profit')
    percentage = fields.Char('%')

    # def view_details(self):
    #     print("jjj")
