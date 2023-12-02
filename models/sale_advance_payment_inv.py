from odoo import api, models

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        # Panggil metode induk untuk membuat faktur seperti biasa
        result = super(SaleAdvancePaymentInv, self).create_invoices()

        # Ambil nilai jamaah_ids dari sale order dan tulis ke invoice
        for order in self.env['sale.order'].browse(self._context.get('active_ids', [])):
            if order.jamaah_ids:
                invoices = self.env['account.move'].search([('invoice_origin', 'in', [order.name])])
                for invoice in invoices:
                    invoice.write({
                        'jamaah_ids': [(6, 0, order.jamaah_ids.ids)]
                    })

        return result
