import base64
import datetime
from calendar import monthrange

from odoo import models, fields, http, api, _
from odoo.http import request


class ReportSendMail(models.TransientModel):
    _name = 'report.send.mail'
    _description = 'Send Report Pdf Via Mail'


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
            {'email_from': "odoobot@taj-limited.odoo.com", "email_to": "kreik.ali@gmail.com",
             "subject": "Aged Reports", "body_html":"<p>Dear Mr. Ali,</p> <p>Please find the attached aged reports for today.</p> <p>best regards.</p>"})
        mail.attachment_ids = [(6, 0, [report_attachment_pay.id, report_attachment_rec.id])]
        mail.send()
