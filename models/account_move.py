# -*- coding: utf-8 -*-

from odoo import models, fields, api # Mandatory


class AccountMove(models.Model):
    _inherit = 'account.move'

    jamaah_ids = fields.Many2many(comodel_name='res.partner', column1='jamaah_ids', column2="jamaah_account_id", required=True)
   