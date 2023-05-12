# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class AccountAsset(models.Model):
    _inherit = 'account.asset'
    
    inventoriable = fields.Boolean(string="Inventoriable", default=True)
    location_id = fields.Many2one(string="Emplacement", comodel_name="stock.location")
    new_location_id = fields.Many2one(string="Nouvel emplacement", comodel_name="stock.location", tracking=True)
    product_id = fields.Many2one(string="Article lié", comodel_name="product.product")
    categ_id = fields.Many2one(related="product_id.categ_id")
    barcode = fields.Char(related="product_id.barcode")
    supplier_id = fields.Many2one(string="Fournisseur", comodel_name="res.partner")
    invoice_name = fields.Char(string="N° de facture")
    year = fields.Char(string="Année")
    asset_categ_id = fields.Many2one(comodel_name='asset.category', string='Nature')
    present = fields.Boolean(string="Est présent", default=False, readonly=True, tracking=True)