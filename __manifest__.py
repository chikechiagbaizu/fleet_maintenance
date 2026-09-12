{
    'name': 'Service Fleet & Maintenance Manager',
    'summary': 'Service Fleet & Maintenance Manager.',
    'description': """A robust backend system to solve real-world operational decay by tracking routine fleet asset servicing.""",
    'author': 'Chike Chiagbaizu',
    'maintainer': 'Chike Chiagbaizu',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Operations',
    'application': True,
    'installable': True,
    'sequence': 1,
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_asset_views.xml',
        'data/rule_fleet_asset_machinery_safety.xml',
        'views/menu.xml',
    ]
}