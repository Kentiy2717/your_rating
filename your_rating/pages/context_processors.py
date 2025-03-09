def menu_items(request):
    return {
        'menu_items': [
            {'title': 'Моя страница', 'url': 'users:index', 'url_name': 'users:index'},
            {'title': 'Рецепты', 'url': 'recipes:index', 'url_name': 'recipes:index'},
            {'title': 'Бочки', 'url': 'casks:index', 'url_name': 'casks:index'},
            {'title': 'Готовые напитки', 'url': 'drinks:index', 'url_name': 'drinks:index'},
            {'title': 'Рейтинг', 'url': 'rating:index', 'url_name': 'rating:index'},
            {'title': 'О проекте', 'url': 'pages:about', 'url_name': 'pages:about'},
            {'title': 'Правила', 'url': 'pages:rules', 'url_name': 'pages:rules'},
        ]
    }
