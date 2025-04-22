from odoo import models, fields

class HrLeaveWizard(models.TransientModel):
    _name = 'hr.leave.wizard'
    _description = 'Leave Wizard'

    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    leave_type = fields.Selection([
        ('paid', 'Paid Leave'),
        ('unpaid', 'Unpaid Leave'),
        ('sick', 'Sick Leave')
    ], string="Leave Type", required=True)
