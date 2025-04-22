from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'  # Kế thừa lại model có sẵn trong Odoo

    department_id = fields.Many2one('hr.department', string='Department')
    payroll_id = fields.Many2one('hr.payroll', string='Payroll')
    attendance_ids = fields.One2many('hr.attendance', 'employee_id', string='Attendances')
