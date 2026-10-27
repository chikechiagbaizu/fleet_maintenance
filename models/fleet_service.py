from odoo import models, fields

class FleetService(models.Model):
    _name = 'fleet.service'
    _description = 'Fleet Service'

    _service_date_constraint = models.Constraint(
        'CHECK(service_date >= fields.Date.today)',
        'Service date cannot be in the past.'
    )

    _cost_constraint = models.Constraint(
        'CHECK(cost >= 1)',
        'Cost cannot be zero or negative.'
    )

    name = fields.Char(string='Service Reference', required=True, default="New")
    asset_id = fields.Many2one(comodel_name='fleet.asset', string='Asset', ondelete='cascade', required=True)
    service_date = fields.Date(default=fields.Date.today, string='Service Date')
    cost = fields.Float(string='Cost', default=1.0)
    notes = fields.Text(string='Maintenance Log')