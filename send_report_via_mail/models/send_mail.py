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
            Transit_fees_Documentation_Fees = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500037')
                 ]).mapped('debit'))
            Transit_fees_Levy_Council_Fee_Nakonde = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500038')
                 ]).mapped('debit'))
            Transit_fees_Levy_Council_Fee_Kapiri = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500039')
                 ]).mapped('debit'))
            Transit_fees_Parking_Security_Fees_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500041')
                 ]).mapped('debit'))
            Transit_fees_Road_Permit = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500042')
                 ]).mapped('debit'))
            Transit_fees_Electronic_Seal = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500045')
                 ]).mapped('debit'))
            Transit_fees_Border_Fees = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500046')
                 ]).mapped('debit'))
            Transit_fees_First_Entry = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500047')
                 ]).mapped('debit'))
            Transit_fees_Lashing_Fees = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500049')
                 ]).mapped('debit'))
            Transit_fees_Abnormalm_Signage = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500050')
                 ]).mapped('debit'))
            Transit_fees_GCLA_Loading_Facilitation_Permit = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500053')
                 ]).mapped('debit'))
            Transit_fees_Weighbridge_Fees = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500055')
                 ]).mapped('debit'))
            Transit_fees_Peage = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500056')
                 ]).mapped('debit'))
            Transit_fees_Levy_Council_Fee_Tunduma = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500058')
                 ]).mapped('debit'))
            Transit_fees_Cargo_Rearrangement = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500059')
                 ]).mapped('debit'))
            Transit_fees_Demurrage_Fee = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500069')
                 ]).mapped('debit'))
            Driver_Trip_Allowance_Expense_Transit = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500096')
                 ]).mapped('debit'))
            Transit_fees_Bond_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500044')
                 ]).mapped('debit'))
            Transit_fees_TollRoad = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500048')
                 ]).mapped('debit'))
            Transit_fees_GCLA_Loading_Facilitation_Other_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500054')
                 ]).mapped('debit'))
            Toll_Gates_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500102')
                 ]).mapped('debit'))
            Late_Exit_Note_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500103')
                 ]).mapped('debit'))
            Return_fees_Container_TAX_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500104')
                 ]).mapped('debit'))
            Carbon_Tax_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500105')
                 ]).mapped('debit'))
            Return_fees_weight_pridje_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500111')
                 ]).mapped('debit'))
            wating_charges_going = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500113')
                 ]).mapped('debit'))
            mbeya = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500073')
                 ]).mapped('debit'))
            kibaha = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500076')
                 ]).mapped('debit'))

            morogoro = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500074')
                 ]).mapped('debit'))
            tunduma = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500075')
                 ]).mapped('debit'))
            account_move_line_return_income = self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', 'in', account_return_income_ids),
                 ])
            Return_fees_Carrier_License = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500061'),
                 ]).mapped('debit'))
            Return_fees_Peage = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500062'),
                 ]).mapped('debit'))
            Return_fees_Cargo_Rearrangement = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500063'),
                 ]).mapped('debit'))
            Return_fees_Radiation_Protection_Fee = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500064'),
                 ]).mapped('debit'))
            Return_fees_Weight_Check_Ndola = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500065'),
                 ]).mapped('debit'))
            Return_fees_Parking_Security_Fees_ret = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500066'),
                 ]).mapped('debit'))
            Return_fees_Levy_Council_Fee_Kapiri = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500067'),
                 ]).mapped('debit'))
            Return_fees_Empty_Container_Offloading_Fees = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500068'),
                 ]).mapped('debit'))
            Return_fees_Visa = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500070'),
                 ]).mapped('debit'))
            Driver_Trip_Allowance_Expense_Return = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500098'),
                 ]).mapped('debit'))
            Return_fees_Weight_Check_Tunduma = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500110'),
                 ]).mapped('debit'))
            Return_fees_Chemical_transportation = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500112'),
                 ]).mapped('debit'))
            Return_fees_Parking_Security_Fees = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '50070'),
                 ]).mapped('debit'))
            Return_fee_Over_Stay = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '50080'),
                 ]).mapped('debit'))
            Return_fees_Entry_Card = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '510071'),
                 ]).mapped('debit'))
            Return_fees_Kanyaka = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '511071'),
                 ]).mapped('debit'))
            Return_fees_Penalty_over_wight = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '512071'),
                 ]).mapped('debit'))
            Transit_fees_Bond = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500044'),
                 ]).mapped('debit'))
            Transit_fees_Road_Toll = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500048'),
                 ]).mapped('debit'))
            Transit_fees_GCLA_Loading_Facilitation_Other = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500054'),
                 ]).mapped('debit'))
            Toll_Gates = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500102'),
                 ]).mapped('debit'))
            Late_Exit_Note = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500103'),
                 ]).mapped('debit'))
            Return_fees_Container_TAX = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500104'),
                 ]).mapped('debit'))
            Carbon_Tax = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500105'),
                 ]).mapped('debit'))
            Return_fees_weight_pridje = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500111'),
                 ]).mapped('debit'))
            wating_charges = sum(self.env['account.move.line'].sudo().search(
                [('order_id', '=', order.order_id.id), ('account_id.code', '=', '500113'),
                 ]).mapped('debit'))

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
            total_credit = 0
            total_debit = 0
            if template_name == 'Return':
                total_credit = sum(account_move_line_return_income.mapped('credit')) + sum(
                    account_move_line.mapped('credit'))
                total_debit = sum(account_move_line_return_income.mapped('debit')) + sum(
                    account_move_line.mapped('debit'))
            if template_name == 'Going':
                total_debit = sum(account_move_line.mapped('debit')) + sum(
                    account_move_line_going_income.mapped('debit'))
                total_credit = sum(account_move_line.mapped('credit')) + sum(
                    account_move_line_going_income.mapped('credit'))
            expenses = total_debit - total_credit
            if order.product_template_id.name != 'Down payment':
                data.append({'order_name': order.order_id.name,
                             'license_plate': order.vehicle_id.license_plate,
                             'root': order.product_template_id.name,
                             'vehicle_id': order.vehicle_id.name,
                             'product_tmpl_id': order.product_template_id.name,
                             'operating_income': op,
                             'account_move_line': account_move_line.ids,
                             'total_fuel': sum(account_move_line.mapped('debit')),
                             'date': order.order_id.date_order,
                             'total_going': sum(
                                 account_move_line_going_income.mapped('debit')) if template_name == 'Going' else 0.0,
                             'total_return': sum(
                                 account_move_line_return_income.mapped('debit')) if template_name == 'Return' else 0.0,
                             'total_return_income': sum(account_move_line_return_income.mapped('debit')),
                             'total_cost': total_debit - total_credit,
                             'cross_profit': op - expenses,
                             'size': order.size,
                             'trip': template_name,
                             'expenses': total_debit - total_credit,
                             "mbeya": mbeya,
                             "kibaha": kibaha,
                             "morogoro": morogoro,
                             "tunduma": tunduma,
                             "Return_fees_Carrier_License": Return_fees_Carrier_License,
                             "Return_fees_Peage": Return_fees_Peage,
                             "Return_fees_Cargo_Rearrangement": Return_fees_Cargo_Rearrangement,
                             "Return_fees_Radiation_Protection_Fee": Return_fees_Radiation_Protection_Fee,
                             "Return_fees_Weight_Check_Ndola": Return_fees_Weight_Check_Ndola,
                             "Return_fees_Parking_Security_Fees": Return_fees_Parking_Security_Fees,
                             "Return_fee_Over_Stay": Return_fee_Over_Stay,
                             "Return_fees_Entry_Card": Return_fees_Entry_Card,
                             "Return_fees_Kanyaka": Return_fees_Kanyaka,
                             "Return_fees_Levy_Council_Fee_Kapiri": Return_fees_Levy_Council_Fee_Kapiri,
                             "Return_fees_Penalty_over_wight": Return_fees_Penalty_over_wight,
                             "Transit_fees_Bond": Transit_fees_Bond,
                             "Transit_fees_Road_Toll": Transit_fees_Road_Toll,
                             "Transit_fees_GCLA_Loading_Facilitation_Other": Transit_fees_GCLA_Loading_Facilitation_Other,
                             "Toll_Gates": Toll_Gates,
                             "Late_Exit_Note": Late_Exit_Note,
                             "Return_fees_Container_TAX": Return_fees_Container_TAX,
                             "Carbon_Tax": Carbon_Tax,
                             "Return_fees_weight_pridje": Return_fees_weight_pridje,
                             "wating_charges": wating_charges,
                             "Return_fees_Empty_Container_Offloading_Fees": Return_fees_Empty_Container_Offloading_Fees,
                             "Return_fees_Chemical_transportation": Return_fees_Chemical_transportation,
                             "Return_fees_Visa": Return_fees_Visa,
                             "Return_fees_Weight_Check_Tunduma": Return_fees_Weight_Check_Tunduma,
                             "Driver_Trip_Allowance_Expense_Return": Driver_Trip_Allowance_Expense_Return,
                             'Return_fees_Parking_Security_Fees_ret': Return_fees_Parking_Security_Fees_ret,
                             "Transit_fees_Documentation_Fees": Transit_fees_Documentation_Fees,
                             "Transit_fees_Levy_Council_Fee_Nakonde": Transit_fees_Levy_Council_Fee_Nakonde,
                             "Transit_fees_Levy_Council_Fee_Kapiri": Transit_fees_Levy_Council_Fee_Kapiri,
                             "Transit_fees_Parking_Security_Fees_going": Transit_fees_Parking_Security_Fees_going,
                             "Transit_fees_Road_Permit": Transit_fees_Road_Permit,
                             "Transit_fees_Electronic_Seal": Transit_fees_Electronic_Seal,
                             "Transit_fees_Border_Fees": Transit_fees_Border_Fees,
                             "Transit_fees_First_Entry": Transit_fees_First_Entry,
                             "Transit_fees_Lashing_Fees": Transit_fees_Lashing_Fees,
                             "Transit_fees_Abnormalm_Signage": Transit_fees_Abnormalm_Signage,
                             "Transit_fees_GCLA_Loading_Facilitation_Permit": Transit_fees_GCLA_Loading_Facilitation_Permit,
                             "Transit_fees_Weighbridge_Fees": Transit_fees_Weighbridge_Fees,
                             "Transit_fees_Peage": Transit_fees_Peage,
                             "Transit_fees_Levy_Council_Fee_Tunduma": Transit_fees_Levy_Council_Fee_Tunduma,
                             "Transit_fees_Cargo_Rearrangement": Transit_fees_Cargo_Rearrangement,
                             "Transit_fees_Demurrage_Fee": Transit_fees_Demurrage_Fee,
                             "Driver_Trip_Allowance_Expense_Transit": Driver_Trip_Allowance_Expense_Transit,
                             "Transit_fees_Bond_going": Transit_fees_Bond_going,
                             "Transit_fees_TollRoad": Transit_fees_TollRoad,
                             "Transit_fees_GCLA_Loading_Facilitation_Other_going": Transit_fees_GCLA_Loading_Facilitation_Other_going,
                             "Toll_Gates_going": Toll_Gates_going,
                             "Late_Exit_Note_going": Late_Exit_Note_going,
                             "Return_fees_Container_TAX_going": Return_fees_Container_TAX_going,
                             "Carbon_Tax_going": Carbon_Tax_going,
                             "Return_fees_weight_pridje_going": Return_fees_weight_pridje_going,
                             "wating_charges_going": wating_charges_going

                             })
        # print("data:::::", data)
        all_1 = {
            'products': data,
        }
        action = self.env.ref('send_report_via_mail.report_profit_and_loss_excel').report_action(self, data=all_1)
        action.update({'close_on_report_download': True})
        return action

    def view_report(self):
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
            total_credit = 0
            total_debit = 0
            if template_name == 'Return':
                total_credit = sum(account_move_line_return_income.mapped('credit')) + sum(
                    account_move_line.mapped('credit'))
                total_debit = sum(account_move_line_return_income.mapped('debit')) + sum(
                    account_move_line.mapped('debit'))
            if template_name == 'Going':
                total_debit = sum(account_move_line.mapped('debit')) + sum(
                    account_move_line_going_income.mapped('debit'))
                total_credit = sum(account_move_line.mapped('credit')) + sum(
                    account_move_line_going_income.mapped('credit'))
            expenses = total_debit - total_credit
            if order.product_template_id.name != 'Down payment':
                print("order.order_id.date_order.date()", order.order_id.date_order.date())
                exist = self.env['report.trip.profit'].sudo().search(
                    [('date', '=', order.order_id.date_order.date()), ('order_id', '=', order.order_id.id)])
                if exist:
                    # for rec in exist:
                    exist.order_id = order.order_id.id
                    exist.truck = order.vehicle_id.license_plate
                    exist.root = order.product_template_id.id
                    exist.trip = template_name
                    exist.size = order.size
                    exist.operating_income = op
                    exist.total_going = sum(
                        account_move_line_going_income.mapped('debit')) if template_name == 'Going' else 0.0
                    exist.total_return = sum(
                        account_move_line_return_income.mapped('debit')) if template_name == 'Return' else 0.0
                    exist.total_fuel = sum(account_move_line.mapped('debit'))
                    exist.expenses = total_debit - total_credit
                    exist.cross_profit = op - expenses
                    exist.percentage = round(((op - expenses) / op * 100), 2) if op != 0 else 0
                else:
                    self.env['report.trip.profit'].sudo().create({'order_id': order.order_id.id,
                                                                  'date': order.order_id.date_order.date(),
                                                                  'truck': order.vehicle_id.license_plate,
                                                                  'root': order.product_template_id.id,
                                                                  'trip': template_name,
                                                                  'size': order.size,
                                                                  'operating_income': op,
                                                                  'total_going': sum(
                                                                      account_move_line_going_income.mapped(
                                                                          'debit')) if template_name == 'Going' else 0.0,
                                                                  'total_return': sum(
                                                                      account_move_line_return_income.mapped(
                                                                          'debit')) if template_name == 'Return' else 0.0,
                                                                  'total_fuel': sum(account_move_line.mapped('debit')),
                                                                  'expenses': total_debit - total_credit,
                                                                  'cross_profit': op - expenses,
                                                                  'percentage': round(((
                                                                                               op - expenses) / op * 100),
                                                                                      2) if op != 0 else 0
                                                                  })
        return {
            'name': 'Report Trip Profit',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'report.trip.profit',
            # 'views': [(treeview_id, 'tree')],
            # 'target': 'new',
        }
