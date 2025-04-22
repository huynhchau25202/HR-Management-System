from odoo import models, fields

class HrAttendance(models.Model):
    _name = 'hr.attendance'
    _description = 'Attendance'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    check_in = fields.Datetime('Check-in')
    check_out = fields.Datetime('Check-out')
    hours_worked = fields.Float('Hours Worked', compute='_compute_hours_worked')

    def _compute_hours_worked(self):
        for record in self:
            if record.check_in and record.check_out:
                delta = record.check_out - record.check_in
                record.hours_worked = delta.total_seconds() / 3600.0
