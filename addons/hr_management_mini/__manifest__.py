{
    'name': 'HR Management Mini',
    'version': '1.0',
    'category': 'Human Resources',
    'depends': ['base', 'hr'],  # Đảm bảo `hr_payroll` được liệt kê ở đây
    'data': [
        'views/hr_management_menu.xml',
        'views/attendance_views.xml',
        'views/department_views.xml',
        'views/employee_views.xml',
        'views/payroll_views.xml',
        'views/hr_employee_action.xml',
        'data/hr_management_data.xml',
        'report/chart_reports.xml',
        'report/payroll_report.xml',
        'security/ir.model.access.csv',
        'wizard/hr_leave_wizard.xml',
    ],
    'installable': True,
    'application': True,
}
