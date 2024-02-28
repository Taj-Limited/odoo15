{
    'name': 'Send Report Via Email',
    'version': '1.0',
    'author': 'Madfox Solutions',
    'website': 'https://madfox.solutions/',
    'category': 'Send Mail Implementation',
    'sequence': 380,
    'summary': 'Send Mail Implementation',
    'description': """Send Report Via Email""",
    'depends': ['payment'],
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'data/report_mail.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}