import datetime
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ReportTajProfitExcel(models.AbstractModel):
    _name = 'report.send_report_via_mail.profit_loss_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        # print('data:::', data['products'])
        bold = workbook.add_format({'bold': True})
        sheet = workbook.add_worksheet("sheet")
        sheet.set_column(0, 11, 25)
        sheet.write(0, 0, 'Truck', bold)
        sheet.write(0, 1, 'Order', bold)
        sheet.write(0, 2, 'Rout', bold)
        sheet.write(0, 3, 'Trip', bold)
        sheet.write(0, 4, 'Size', bold)
        sheet.write(0, 5, 'Year', bold)
        sheet.write(0, 6, 'Operating Income', bold)
        sheet.write(0, 7, 'Total Going', bold)
        sheet.write(0, 8, 'Total Return', bold)
        sheet.write(0, 9, 'Total Fuel', bold)
        sheet.write(0, 10, 'Total Cost', bold)
        sheet.write(0, 11, 'Cross Profit', bold)
        sheet.write(0, 12, '%', bold)

        # sheet.write(0, 5, 'Jt I sh', bold)
        # sheet.write(0, 6, 'Jt I Ml', bold)
        # sheet.write(0, 7, 'Jt I Ml Liq', bold)
        # sheet.write(0, 8, 'Last Purchase Date', bold)
        # sheet.write(0, 9, 'Out Of Stock Date', bold)
        # sheet.write(0, 10, 'Days Of Published', bold)
        # sheet.write(0, 11, 'Sales Price', bold)
        # sheet.write(0, 12, 'Quantity', bold)
        row = 0
        for obj in data['products']:
            row += 1
            sheet.write(row, 0, obj['license_plate'])
            sheet.write(row, 1, obj['order_name'])
            sheet.write(row, 2, obj['root'])
            sheet.write(row, 3, obj['trip'])
            sheet.write(row, 4, obj['size'])
            sheet.write(row, 5, obj['date'])
            sheet.write(row, 6, obj['operating_income'])
            sheet.write(row, 7, obj['total_going'])
            sheet.write(row, 8, obj['total_return'])
            sheet.write(row, 9, obj['total_fuel'])
            sheet.write(row, 10, obj['total_cost'])
            sheet.write(row, 11, obj['cross_profit'])
            sheet.write(row, 12, obj['cross_profit'] / obj['operating_income'] if obj['operating_income'] != 0 else 0)
