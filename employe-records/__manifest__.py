{
    'name': 'Employee Records system',
    'summary': """This module will add a record to store Employee details""",
    'description': """This module will add a record to store Employee details""",
    'category': 'Tools',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/delete_dialouge_box_wizard.xml',
        'views/employee_view.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,

}