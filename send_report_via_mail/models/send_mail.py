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
        file_receivable = report_payable.get_pdf(receivable_options)
        ir_values_payable = {
            'name': 'Invoice Report',
            'type': 'binary',
            'datas': base64.b64encode(file_payable),
            'store_fname': base64.b64encode(file_payable),
            'mimetype': 'application/pdf',
            'res_model': 'account.move',
        }
        ir_values_receivable = {
            'name': 'Invoice Report',
            'type': 'binary',
            'datas': base64.b64encode(file_receivable),
            'store_fname': base64.b64encode(file_receivable),
            'mimetype': 'application/pdf',
            'res_model': 'account.move',
        }
        report_attachment_pay = self.env['ir.attachment'].sudo().create(ir_values_payable)
        report_attachment_rec = self.env['ir.attachment'].sudo().create(ir_values_receivable)

        email_template = self.env.ref('send_report_via_mail.email_template_report_pdf')
        email_template.attachment_ids = [(6, 0, [report_attachment_pay.id, report_attachment_rec.id])]
        email_template.send_mail(self.id)
        # empty the mail attachments
        email_template.attachment_ids = [(5, 0, 0)]
        mail = self.env['mail.mail'].sudo().browse(email_template.id)
        mail.send()
