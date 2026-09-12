from odoo import models, fields

class FleetService(models.Model):
    _name = 'fleet.service'
    _description = 'Fleet Service'

    asset_id = fields.Many2one(comodel_name='fleet.asset', string='Asset ID', ondelete='cascade')
    service_date = fields.Date(default=fields.Date.today(), string='Service Date')
    cost = fields.Float(string='Cost')
    notes = fields.Text(string='Maintenance Logs')