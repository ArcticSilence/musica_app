{
    'name': 'Aplicación de gestión de discos',
    'description': 'Gestiona discos, grupos, artistas, canciones, etc..',
    'author': ['Guillermo Bort', 'Nacho Sanz', 'Álvaro Sobrino'],
    'depends': ['base'],
    'application': True,
    'installable': True,
    'data': [
        'security/musica_security.xml',
        'security/ir.model.access.csv',
        'views/musica_menu.xml',
        'views/disco_view.xml',
        'views/grupo_view.xml',
        # 'views/companyia_view.xml',
        # 'views/artista_view.xml',
        # 'views/cancion_view.xml',
    ],
    'demo': [],
}
