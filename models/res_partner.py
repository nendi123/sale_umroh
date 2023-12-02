# -*- coding: utf-8 -*-

from odoo import models, fields, api # Mandatory


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_id = fields.Many2many(comodel_name='sale.order', column2='jamaah_ids', column1="sale_id")
    jamaah_account_id = fields.Many2many(comodel_name='account.move', column2='jamaah_ids', column1="jamaah_account_id")
    nik = fields.Char()
    no_ktp = fields.Char()
    no_wa_darurat = fields.Char()
    foto_3x4 = fields.Image()
    foto_4x6 = fields.Image()
    no_passport = fields.Char()
    tgl_terbit = fields.Date()
    tgl_expired = fields.Date()
    kantor_terbit = fields.Char()

    scan_foto_passport = fields.Binary()
    scan_foto_ktp = fields.Binary()
    scan_foto_kk = fields.Binary()
    scan_akta_kelahiran = fields.Binary()
    scan_buku_nikah = fields.Binary()
    scan_ijazah = fields.Binary()
    scan_buku_vaksin = fields.Binary()