{
    'name': "custom_pos",
    'author': "shahd mohamed",
    'category': "",
    'version': "17.0.0.1.0",
    'depends': [
        'base','mail','contacts','point_of_sale'
    ],
    'data': [
        'views/partner_view_inherit_pos.xml',



    ],


    'assets': {
        'point_of_sale._assets_pos': [
            'views/point_of_sale_view.xml',
            'custom_pos/static/src/components/owlView/owlView.js',



        ],
    },
    'application': True,

}