{
    'name': 'Pet Shop',
    'version': '14.0.1.0',
    'category': 'Sales',
    'summary': 'Site Pet Shop',
    'description': 'Loja para loja de pets',
    'author': 'Daniel Soares',
    'maintainer': 'Daniel Soares',
    'application': True,
    'installable': True,
    'license': 'AGPL-3',
    'data': [
        'views/res_partner_views.xml',
        'views/pet_shop_type_views.xml',
        'views/pet_shop_course_views.xml',
        'views/pet_shop_vaccine.xml',
        'views/pet_shop_pet_views.xml',
        'views/pet_shop_menus.xml',
    ],
    'depends': ['contacts'],
}

