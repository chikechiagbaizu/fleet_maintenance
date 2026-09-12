from odoo import models, fields

class FleetAsset(models.Model):
    _name = 'fleet.asset'
    _description = 'Fleet Asset'

    name = fields.Char(string='Tracking Name')
    asset_type = fields.Selection(selection=[
        ('vehicle','vehicle'),
        ('machinery','Industrial Machinery'),
    ], string='Asset Type')
    assigned_employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee ID')
    service_history_ids = fields.One2many(comodel_name='fleet.service', inverse_name='asset_id', string='Service History IDs')