from odoo import models, api, fields


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    sale_order_id = fields.Many2one('sale.order', 'Sale Order')

    def action_create_invoice(self):
        action = super(PurchaseOrderInherit, self).action_create_invoice()
        # account_move_id = self.env['account.move'].sudo().search([("purchase_id", "=", self.id)])
        # print("account_move_id", account_move_id)
        for rec in self.sale_order_id.order_line:
            for rec_line in self.invoice_ids[0].line_ids:
                rec_line.container_num = rec.container_num
                rec_line.file_name = rec.file_name
                rec_line.consignee = rec.consignee
                rec_line.weight = rec.weight
                rec_line.size = rec.size
                rec_line.srn = rec.srn
                rec_line.vehicle_id = rec.vehicle_id
