# -*- coding: utf-8 -*-
{
    'name'          : "Ml Data",
    'description'   : """Mall Data Resource for payment bill transporting Analysis""",
    'author'        : "Aung Myo Swe",
    'summary'       : """Mall Data Resource""",
    
    'website'       : "www.zandotech.com",
    'category'      : 'base',
    'version'       : '12.1.0.1',
    'depends'       : ['base','uom','web'],
    'data'          : [
        'security/ir.model.access.csv',
        'views/mall_view.xml',
        'views/floor_views.xml',
        'views/space_view.xml',
        'static/custom_css_view.xml',
        'data/ml_data.xml'
    ],
    'installable'   : True,
    'application'   : True,
}
