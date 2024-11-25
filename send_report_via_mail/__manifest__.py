{
    'name': 'Send Report Via Email',
    'version': '17.0',
    'author': 'Madfox Solutions',
    'website': 'https://madfox.solutions/',
    'category': 'Send Mail Implementation',
    'sequence': 380,
    'summary': 'Send Mail Implementation',
    'description': """Send Report Via Email""",
    'depends': ['payment'],
    'depends': ['account', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/report_mail.xml',
        'views/send_mail.xml',
        'reports/report_profit_and_loss_views.xml',
        'views/report_trip_profit_views.xml'
    ],
    'application': True,
    'license': 'LGPL-3',
}
