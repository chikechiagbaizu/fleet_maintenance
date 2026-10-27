{
    'name': 'Service Fleet & Maintenance Manager',
    'summary': 'Service Fleet & Maintenance Manager.',
    'author': 'Chike Chiagbaizu',
    'maintainer': 'Chike Chiagbaizu',
    'version': '19.0.1.0.1',
    'license': 'LGPL-3',
    'category': 'Maintenance',
    'application': True,
    'installable': True,
    'sequence': 20,
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'security/res_group.xml',
        'security/ir.model.access.csv',
        'security/ir_rule_fleet_asset.xml',
        'security/ir_rule_fleet_service.xml',
        'views/fleet_asset_form_view.xml',
        'views/fleet_asser_list_view.xml',
        'views/fleet_asset_action.xml',
        'views/fleet_service_form_view.xml',
        'views/fleet_service_list_view.xml',
        'views/fleet_service_action.xml',
        'views/menu.xml',
    ]
}