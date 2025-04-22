from odoo import models, fields

class HRDepartment(models.Model):
    _name = 'hr.department'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True)

    # Thêm trường member_ids
    member_ids = fields.Many2many('res.users', 'department_user_rel', 'department_id', 'user_id', string='Members')
