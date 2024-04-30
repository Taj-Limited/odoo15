import base64
import datetime
from calendar import monthrange

from odoo import models, fields, http, api, _
from odoo.http import request


class ReportSendMail(models.TransientModel):
    _name = 'report.send.mail'
    _description = 'Send Report Pdf Via Mail'

    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')

    def send_email_with_pdf_attach(self):
        report_payable = self.env["account.aged.payable"]
        report_receivable = self.env["account.aged.receivable"]
        payable_options = report_payable._get_options()
        receivable_options = report_receivable._get_options()
        file_payable = report_payable.get_pdf(payable_options)
        file_receivable = report_receivable.get_pdf(receivable_options)
        ir_values_payable = {
            'name': 'aged payable.pdf',
            'type': 'binary',
            'datas': base64.b64encode(file_payable),
            'store_fname': base64.b64encode(file_payable),
            'mimetype': 'application/pdf',
            'res_model': 'account.move',
        }
        ir_values_receivable = {
            'name': 'aged receivable.pdf',
            'type': 'binary',
            'datas': base64.b64encode(file_receivable),
            'store_fname': base64.b64encode(file_receivable),
            'mimetype': 'application/pdf',
            'res_model': 'account.move',
        }
        report_attachment_pay = self.env['ir.attachment'].sudo().create(ir_values_payable)
        report_attachment_rec = self.env['ir.attachment'].sudo().create(ir_values_receivable)
        mail = request.env['mail.mail'].sudo().create(
            {'email_from': "odoobot@taj-limited.odoo.com", "email_to": "kreik.ali@gmail.com", "email_cc": "nour.m@madfox.me; Moustapha@madfoxme.com; souzan.s@madfoxme.com",
             "subject": "Aged Reports",
             "body_html": "<p>Dear Mr. Ali,</p> <p>Please find the attached aged reports for today.</p> <p>best regards.</p>"})
        mail.attachment_ids = [(6, 0, [report_attachment_pay.id, report_attachment_rec.id])]
        mail.send()
        # return mail

    def convert_date_to_datetime(self, from_date, to_date):
        my_time = datetime.datetime.min.time()
        max_time = datetime.datetime.max.time()
        from_date = datetime.datetime.combine(from_date, my_time)
        to_date = datetime.datetime.combine(to_date, max_time)
        return from_date, to_date

    def send_report(self):
        # date_from = '03-04-23'
        # date_to = '03/05/2023'
        date = datetime.datetime.now()
        date_from_d = datetime.datetime.strptime('02/01/24', '%m/%d/%y').date()
        date_to_d = datetime.datetime.strptime('03/03/24', '%m/%d/%y').date()
        from_d, to_d = self.convert_date_to_datetime(from_date=self.from_date, to_date=self.to_date)
        orders = self.env['sale.order'].sudo().search([('date_order', '>', from_d), ('date_order', '<=', to_d)])
        order_ids = []
        data = []
        typ_of_account_income = self.env['account.account.type'].sudo().search([('name', '=', 'Income')])
        typ_of_account_cost_of_revenue = self.env['account.account.type'].sudo().search(
            [('name', '=', 'Cost of Revenue')])
        account_fuel_ids = ['500073', '500074', '500075', '500076', '500077']
        account_return_income_ids = ['500061', '500062', '500063', '500064', '500065', '500066', '500067', '500068',
                                     '500070', '500098', '500110', '500112', '50070', '50080', '510071', '511071',
                                     '512071', '500044', '500048', '500054', '500102', '500103', '500104', '500105',
                                     '500111', '500113']
        account_going_of_revenue_ids = ['500037', '500038', '500039', '500041', '500042', '500045', '500046', '500047',
                                        '500049', '500050', '500053', '500055', '500056', '500058', '500059', '500069',
                                        '500096', '500044', '500048', '500054', '500102', '500103', '500104', '500105',
                                        '500111', '500113']
        for order in orders.order_line:
            order_ids.append(order)
            account_move_line = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', 'in', account_fuel_ids)
                 ])
            account_move_line_return_income = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', 'in', account_return_income_ids),
                 ])
            account_move_line_going_income = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', 'in', account_going_of_revenue_ids),
                 ])
            if len(
                    order.order_id.invoice_ids) > 0:
                op = order.order_id.invoice_ids[0].amount_total_signed
            else:
                op = 0.0
            template_name = 'Return'
            if order.product_template_id.name:
                template_name = 'Going' if 'Dar' in order.product_template_id.name.split('-')[0] else 'Return'
            else:
                template_name = 'Return'
            total_credit = sum(account_move_line_return_income.mapped('credit')) + sum(
                account_move_line.mapped('credit')) + sum(account_move_line_going_income.mapped('credit'))
            data.append({'order_name': order.order_id.name,
                         'license_plate': order.vehicle_id.license_plate,
                         'root': order.product_template_id.name,
                         'vehicle_id': order.vehicle_id.name,
                         'product_tmpl_id': order.product_template_id.name,
                         'operating_income': op,
                         'account_move_line': account_move_line.ids,
                         'total_fuel': sum(account_move_line.mapped('debit')),
                         'date': order.order_id.date_order,
                         'total_going': sum(account_move_line_going_income.mapped('debit')),
                         'total_return': sum(account_move_line_return_income.mapped('debit')),
                         'total_return_income': sum(account_move_line_return_income.mapped('debit')),
                         'total_cost': sum(account_move_line_return_income.mapped('debit')) + sum(
                             account_move_line.mapped('debit')) + sum(account_move_line_going_income.mapped('debit')),
                         'cross_profit': op - (
                                 sum(account_move_line_return_income.mapped('debit')) + sum(
                             account_move_line.mapped('debit')) + sum(account_move_line_going_income.mapped('debit'))),
                         'size': order.size,
                         'trip': template_name,
                         'expenses': (sum(account_move_line_return_income.mapped('debit')) + sum(
                             account_move_line.mapped('debit')) + sum(
                             account_move_line_going_income.mapped('debit'))) - total_credit

                         })
        # print("data:::::", data)
        all_1 = {
            'products': data,
        }
        action = self.env.ref('send_report_via_mail.report_profit_and_loss_excel').report_action(self, data=all_1)
        action.update({'close_on_report_download': True})
        return action
