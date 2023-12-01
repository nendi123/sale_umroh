# -*- coding: utf-8 -*-

from odoo import models, fields, api # Mandatory


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    jamaah_ids = fields.Many2many(comodel_name='res.partner', column1='jamaah_ids', column2="sale_id")
   