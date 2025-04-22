from odoo import models, fields

class HrPayroll(models.Model):
    _name = 'hr.payroll'
    _description = 'Payroll'

    name = fields.Char('Payroll Name', required=True)
    employee_ids = fields.One2many('hr.employee', 'payroll_id', string='Employees')
    basic_salary = fields.Float('Basic Salary')
    bonuses = fields.Float('Bonuses')
    total_salary = fields.Float(compute='_compute_total_salary', string='Total Salary')

    def _compute_total_salary(self):
        for record in self:
            record.total_salary = record.basic_salary + record.bonuses
