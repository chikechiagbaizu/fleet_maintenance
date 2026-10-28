from odoo import api, fields, models
from datetime import timedelta  

class FleetAsset(models.Model):
    _name = 'fleet.asset'
    _description = 'Fleet Asset'

    ASSET_TYPES = [
        ('it_computing','IT and Computing Equipment'),
        ('vehicle','Vehicle'),
        ('machinery','Industrial Machinery'),
    ]

    name = fields.Char(string='Asset Name', required=True, default="New")
    assigned_employee_id = fields.Many2one(comodel_name='hr.employee', string='Staff')
    license_plate = fields.Char(string="License Plate")
    service_intervals_days = fields.Integer(string='Service Interval Days')
    service_history_ids = fields.One2many(comodel_name='fleet.service', inverse_name='asset_id', string='Service History')
    asset_type = fields.Selection(selection=ASSET_TYPES, string='Asset Type', default="it_computing", required=True)
    last_service_date = fields.Date(string='Last Service Date')
    next_service_date = fields.Date(string='Next Service Date', compute='_compute_next_service_date', inverse="_inverse_service_interval_days", store=True)
    is_overdue = fields.Boolean(string='Is Overdue?', default=False)
    active = fields.Boolean(default=True)

    @api.depends('service_intervals_days','last_service_date')
    def _compute_next_service_date(self):
        for record in self:
            if record.service_intervals_days > 0 and record.last_service_date:
                record.next_service_date = record.last_service_date + timedelta(days=record.service_intervals_days).days
            else:
                record.next_service_date = False
    
    def _inverse_service_interval_days(self):
        for record in self:
            if record.last_service_date and record.next_service_date:
                record.service_intervals_days = (record.next_service_date - record.last_service_date).days