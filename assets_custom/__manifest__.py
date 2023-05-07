# -*- coding: utf-8 -*-
{
    'name': 'Assets R&B Consulting',
    'version': '16.0.1.0.0',
    "summary": "Assets R&B Consulting",
    "author": "R&B Consulting",
    "website": "https://www.r-bconsulting.com",
    'license': 'AGPL-3',
    "category": "Generic",
    'depends': [
        'base',
        'account_asset',
        'stock',
        'product'
    ],
    'data': [
        'views/account_asset_view.xml',
        'views/product_category_view.xml',
        'views/asset_category_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}
