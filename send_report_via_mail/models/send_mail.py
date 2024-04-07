import base64
import datetime
from calendar import monthrange

from odoo import models, fields, http, api, _
from odoo.http import request
import logging


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
        self.env.cr.commit()
        _logger = logging.getLogger(__name__)
        _logger.info(f"report_attachment_pay: {report_attachment_pay}")
        _logger.info(f"report_attachment_rec: {report_attachment_rec}")
        mail = request.env['mail.mail'].sudo().create(
            {'email_from': "odoobot@taj-limited.odoo.com", "email_to": "kreik.ali@gmail.com",
             "email_cc": "nour.m@madfoxme.com; Moustapha@madfoxme.com; souzan.s@madfoxme.com",
             "subject": "Aged Reports",
             "body_html": "<p>Dear Mr. Ali,</p> <p>Please find the attached aged reports for today.</p> <p>best regards.</p>"})
        # mail.attachment_ids = [(6, 0, [report_attachment_pay.id, report_attachment_rec.id])]
        mail.attachment_ids = [report_attachment_pay.id, report_attachment_rec.id]
        mail.send()

    def convert_date_to_datetime(self, from_date, to_date):
        my_time = datetime.datetime.min.time()
        max_time = datetime.datetime.max.time()
        from_date = datetime.datetime.combine(from_date, my_time)
        to_date = datetime.datetime.combine(to_date, max_time)
        return from_date, to_date

    def send_report(self):
        date_from = '03-04-23'
        date_to = '03/05/2023'
        date = datetime.datetime.now()
        date_from_d = datetime.datetime.strptime('02/01/24', '%m/%d/%y').date()
        date_to_d = datetime.datetime.strptime('03/03/24', '%m/%d/%y').date()
        print('from_date', self.from_date)
        print('to_date', self.to_date)
        from_d, to_d = self.convert_date_to_datetime(from_date=self.from_date, to_date=self.to_date)
        print("from_d", from_d)
        print("to_d", to_d)
        orders = self.env['sale.order'].sudo().search([('date_order', '>', from_d), ('date_order', '<=', to_d)])
        order_ids = []
        data = []
        typ_of_account_income = self.env['account.account.type'].sudo().search([('name', '=', 'Income')])
        typ_of_account_cost_of_revenue = self.env['account.account.type'].sudo().search(
            [('name', '=', 'Cost of Revenue')])
        fuel_ids = self.env['account.account'].sudo().search([('name', 'like', 'Fuel')])
        account_fuel_ids = [fuel.id for fuel in fuel_ids]
        return_income_ids = self.env['account.account'].sudo().search(
            [('name', 'like', 'Return'), ('user_type_id', '=', typ_of_account_income.id)])
        account_return_income_ids = [fuel.id for fuel in return_income_ids]
        return_cost_of_revenue_ids = self.env['account.account'].sudo().search(
            [('name', 'like', 'Return'), ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        account_return_cost_of_revenue_ids = [fuel.id for fuel in return_cost_of_revenue_ids]
        account_documentation_fees = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Documentation Fees'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        account_documentation_fees_ids = [fee.id for fee in account_documentation_fees]
        account_levy_council_fees = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Levy Council Fee - Nakonde'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        account_levy_council_fees_ids = [levy.id for levy in account_levy_council_fees]
        account_Tunduma = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Levy Council Fee - Tunduma'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        account_Kapiri = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Levy Council Fee - Kapiri'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        account_Parking_Security_Fees = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Parking & Security Fees'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        account_Road_Permit = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Road Permit'), ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Electronic_Seal = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Electronic Seal'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_Border_Fees = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Border Fees'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_Bond = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Border Fees'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        First_Entry = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - First Entry'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_Road_Toll = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Road Toll'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_Demurrage_Fee = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Demurrage Fee'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_Lashing_Fees = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Lashing Fees'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Abnormalm_Signage = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Abnormalm - Signage'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_GCLA_Loading_Facilitation_Other = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - GCLA Loading Facilitation - Other'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Driver_Trip_Allow_ance_Expense_Transit = self.env['account.account'].sudo().search(
            [('name', 'like', 'Driver Trip Allowance Expense -Transit'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Toll_Gates = self.env['account.account'].sudo().search(
            [('name', 'like', 'Toll Gates'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Late_Exit_Note = self.env['account.account'].sudo().search(
            [('name', 'like', 'Late Exit Note'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_Cargo_Rearrangement = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Cargo Rearrangement'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Carbon_Tax = self.env['account.account'].sudo().search(
            [('name', 'like', 'Carbon Tax'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        Transit_fees_Peage = self.env['account.account'].sudo().search(
            [('name', 'like', 'Transit fees - Peage -'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        KAWACHA = self.env['account.account'].sudo().search(
            [('name', 'like', 'KAWACHA'),
             ('user_type_id', '=', typ_of_account_cost_of_revenue.id)])
        for order in orders.order_line:
            print("order.product_template_id.name.split('-')[0]", order.product_template_id.name.split('-')[0])
            order_ids.append(order)
            account_move_line = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_fuel_ids)
                 ])
            account_move_line_return_income = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_return_income_ids),
                 ])
            account_move_line_return_cost_of_revenue = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_return_cost_of_revenue_ids),
                 ])
            account_move_line_documentation_fees_cost_of_revenue = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_documentation_fees_ids),
                 ])
            account_move_line_levy_council_fees_cost_of_revenue = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_levy_council_fees_ids),
                 ])
            account_move_line_account_Tunduma_cost_of_revenue = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_Tunduma.ids),
                 ])
            account_move_line_account_Kapiri_cost_of_revenue = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_Kapiri.ids),
                 ])
            account_move_line_account_Parking_Security_Fees_cost_of_revenue = self.env[
                'account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_Parking_Security_Fees.ids),
                 ])
            account_move_line_account_Road_Permit = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', account_Road_Permit.ids),
                 ])
            account_move_line_account_Electronic_Seal = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Electronic_Seal.ids),
                 ])
            account_move_line_Transit_fees_Border_Fees = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Transit_fees_Border_Fees.ids),
                 ])
            account_move_line_Transit_fees_Bond = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Transit_fees_Bond.ids),
                 ])
            account_move_line_Transit_First_Entry = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', First_Entry.ids),
                 ])
            account_move_line_Transit_fees_Road_Toll = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Transit_fees_Road_Toll.ids),
                 ])
            account_move_line_Transit_fees_Demurrage_Fee = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Transit_fees_Demurrage_Fee.ids),
                 ])
            account_move_line_Transit_fees_Lashing_Fees = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Transit_fees_Lashing_Fees.ids),
                 ])
            account_move_line_Abnormalm_Signage = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Abnormalm_Signage.ids),
                 ])
            account_move_lineTransit_fees_GCLA_Loading_Facilitation_Other = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id),
                 ('account_id', 'in', Transit_fees_GCLA_Loading_Facilitation_Other.ids),
                 ])
            account_move_line_Driver_Trip_Allow_ance_Expense_Transit = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Driver_Trip_Allow_ance_Expense_Transit.ids),
                 ])
            account_move_line_Toll_Gates = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Toll_Gates.ids),
                 ])
            account_move_line_Late_Exit_Note = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Late_Exit_Note.ids),
                 ])
            account_move_line_Transit_fees_Cargo_Rearrangement = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Transit_fees_Cargo_Rearrangement.ids),
                 ])
            account_move_line_Carbon_Tax = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Carbon_Tax.ids),
                 ])
            account_move_line_Transit_fees_Peage = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', Transit_fees_Peage.ids),
                 ])
            account_move_line_KAWACHA = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id', 'in', KAWACHA.ids),
                 ])
            total_going = sum(
                account_move_line_documentation_fees_cost_of_revenue.mapped('debit')) + sum(
                account_move_line_levy_council_fees_cost_of_revenue.mapped('debit')) + sum(
                account_move_line_account_Tunduma_cost_of_revenue.mapped('debit')) + sum(
                account_move_line_account_Kapiri_cost_of_revenue.mapped('debit')) + sum(
                account_move_line_account_Parking_Security_Fees_cost_of_revenue.mapped('debit')) + sum(
                account_move_line_account_Road_Permit.mapped('debit')) + sum(
                account_move_line_account_Electronic_Seal.mapped('debit')) + sum(
                account_move_line_Transit_fees_Border_Fees.mapped('debit')) + sum(
                account_move_line_Transit_First_Entry.mapped('debit')) + sum(
                account_move_line_Transit_fees_Bond.mapped('debit')) + sum(
                account_move_line_Transit_fees_Road_Toll.mapped('debit')) + sum(
                account_move_line_Transit_fees_Demurrage_Fee.mapped('debit')) + sum(
                account_move_line_Transit_fees_Lashing_Fees.mapped('debit')) + sum(
                account_move_line_Abnormalm_Signage.mapped('debit')) + sum(
                account_move_lineTransit_fees_GCLA_Loading_Facilitation_Other.mapped('debit')) + sum(
                account_move_line_Driver_Trip_Allow_ance_Expense_Transit.mapped('debit')) + sum(
                account_move_line_Toll_Gates.mapped('debit')) + sum(
                account_move_line_Late_Exit_Note.mapped('debit')) + sum(
                account_move_line_Transit_fees_Cargo_Rearrangement.mapped('debit')) + sum(
                account_move_line_Carbon_Tax.mapped('debit')) + sum(
                account_move_line_Transit_fees_Peage.mapped('debit')) + sum(account_move_line_KAWACHA.mapped('debit'))
            data.append({'order_name': order.order_id.name,
                         'license_plate': order.vehicle_id.license_plate,
                         'root': order.product_template_id.name,
                         'vehicle_id': order.vehicle_id.name,
                         'product_tmpl_id': order.product_template_id.name,
                         'operating_income': order.order_id.invoice_ids[0].amount_total_signed if len(
                             order.order_id.invoice_ids) > 0 else 0.0,
                         'account_move_line': account_move_line.ids,
                         'total_fuel': sum(account_move_line.mapped('debit')),
                         'date': order.order_id.date_order,
                         'total_going': total_going,
                         'total_return': sum(account_move_line_return_income.mapped('credit')) + sum(
                             account_move_line_return_cost_of_revenue.mapped('debit')),
                         'total_return_income': sum(account_move_line_return_income.mapped('credit')),
                         'total_return_cost_of_revenue': sum(account_move_line_return_cost_of_revenue.mapped('debit')),
                         'total_document_cost_of_revenue': sum(
                             account_move_line_documentation_fees_cost_of_revenue.mapped('debit')),
                         'total_levy_council_fee_cost_of_revenue': sum(
                             account_move_line_levy_council_fees_cost_of_revenue.mapped('debit')),
                         'total_account_move_line_account_Tunduma_cost_of_revenue': sum(
                             account_move_line_account_Tunduma_cost_of_revenue.mapped('debit')),
                         'total_account_move_line_account_Kapiri_cost_of_revenue': sum(
                             account_move_line_account_Kapiri_cost_of_revenue.mapped('debit')),
                         'total_account_move_line_account_Parking_Security_Fees_cost_of_revenue': sum(
                             account_move_line_account_Parking_Security_Fees_cost_of_revenue.mapped('debit')),
                         'account_move_line_account_Road_Permit': sum(
                             account_move_line_account_Road_Permit.mapped('debit')),
                         'account_move_line_account_Electronic_Seal': sum(
                             account_move_line_account_Electronic_Seal.mapped('debit')),
                         'account_move_line_Transit_fees_Border_Fees': sum(
                             account_move_line_Transit_fees_Border_Fees.mapped('debit')),
                         'account_move_line_Transit_fees_Bond': sum(
                             account_move_line_Transit_fees_Bond.mapped('debit')),
                         'account_move_line_Transit_First_Entry': sum(
                             account_move_line_Transit_First_Entry.mapped('debit')),
                         'account_move_line_Transit_fees_Road_Toll': sum(
                             account_move_line_Transit_fees_Road_Toll.mapped('debit')),
                         'account_move_line_Transit_fees_Demurrage_Fee': sum(
                             account_move_line_Transit_fees_Demurrage_Fee.mapped('debit')),
                         'account_move_line_Transit_fees_Lashing_Fees': sum(
                             account_move_line_Transit_fees_Lashing_Fees.mapped('debit')),
                         'account_move_line_Abnormalm_Signage': sum(
                             account_move_line_Abnormalm_Signage.mapped('debit')),
                         'account_move_lineTransit_fees_GCLA_Loading_Facilitation_Other': sum(
                             account_move_lineTransit_fees_GCLA_Loading_Facilitation_Other.mapped('debit')),
                         'account_move_line_Driver_Trip_Allow_ance_Expense_Transit': sum(
                             account_move_line_Driver_Trip_Allow_ance_Expense_Transit.mapped('debit')),
                         'account_move_line_Toll_Gates': sum(
                             account_move_line_Toll_Gates.mapped('debit')),
                         'account_move_line_Late_Exit_Note': sum(account_move_line_Late_Exit_Note.mapped('debit')),
                         'account_move_line_Transit_fees_Cargo_Rearrangement': sum(
                             account_move_line_Transit_fees_Cargo_Rearrangement.mapped('debit')),
                         'account_move_line_Carbon_Tax': sum(account_move_line_Carbon_Tax.mapped('debit')),
                         'account_move_line_Transit_fees_Peage': sum(
                             account_move_line_Transit_fees_Peage.mapped('debit')),
                         'account_move_line_KAWACHA': sum(account_move_line_KAWACHA.mapped('debit')),
                         'total_cost': sum(account_move_line_return_income.mapped('credit')) + sum(
                             account_move_line_return_cost_of_revenue.mapped('debit')) + sum(
                             account_move_line.mapped('debit')) + total_going,
                         'cross_profit': (order.order_id.invoice_ids[0].amount_total_signed if len(
                             order.order_id.invoice_ids) > 0 else 0.0) - (
                                                 sum(account_move_line_return_income.mapped('credit')) + sum(
                                             account_move_line_return_cost_of_revenue.mapped('debit')) + sum(
                                             account_move_line.mapped('debit')) + total_going),
                         'size': order.size,
                         'trip': 'Going' if 'Dar' in order.product_template_id.name.split('-')[0] else 'Return'

                         })
        print("data:::::", data)
        all_1 = {
            'products': data,
        }
        action = self.env.ref('send_report_via_mail.report_profit_and_loss_excel').report_action(self, data=all_1)
        action.update({'close_on_report_download': True})
        return action
