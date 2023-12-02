# -*- coding: utf-8 -*-

from odoo import models, fields, api # Mandatory


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    jamaah_ids = fields.Many2many(comodel_name='res.partner', column1='jamaah_ids', column2="sale_id")
   
    # def action_create_invoice(self):
    #     # Lakukan operasi membuat invoice seperti biasa
    #     invoice = super(SaleOrder, self).action_create_invoice()

    #     # Debugging - Cetak nilai jamaah_ids
    #     print(f"Jamaah IDs from Sale Order: {self.jamaah_ids}")

    #     # Ambil nilai jamaah_ids dari sale order dan tulis ke invoice
    #     if self.jamaah_ids:
    #         invoice.write({
    #             'jamaah_ids': [(6, 0, self.jamaah_ids.ids)]
    #         })

    #     # Debugging - Cetak nilai jamaah_ids setelah ditulis ke invoice
    #     print(f"Jamaah IDs after writing to Invoice: {invoice.jamaah_ids}")

    #     return invoice