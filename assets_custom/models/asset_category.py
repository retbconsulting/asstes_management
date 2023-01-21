# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class AssetCategory(models.Model):
    _name = 'asset.category'

    name = fields.Char(string="Libellé")