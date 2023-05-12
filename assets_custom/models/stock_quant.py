# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    
    def action_apply_inventory(self):
        ### Look for related Asset
        for record in self:
            related_asset = self.env['account.asset'].search([('product_id', '=', record.product_id.id)], limit=1)
            if related_asset and not record.inventory_quantity:
                related_asset.write({'present' : True, 'new_location_id' : record.location_id.id})
                self.write({'inventory_quantity' : 1})
        return super(StockQuant, self).action_apply_inventory()