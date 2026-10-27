from odoo import models, fields

class FleetAsset(models.Model):
    _name = 'fleet.asset'
    _description = 'Fleet Asset'

    ASSET_TYPES = [
        ('it_computing','IT and Computing Equipment'),
        ('vehicle','Vehicle'),
        ('machinery','Industrial Machinery'),
    ]

    name = fields.Char(string='Asset Name', required=True, default="New")
    asset_type = fields.Selection(selection=ASSET_TYPES, string='Asset Type', default="it_computing", required=True)
    assigned_employee_id = fields.Many2one(comodel_name='hr.employee', string='Staff')
    service_history_ids = fields.One2many(comodel_name='fleet.service', inverse_name='asset_id', string='Service History')