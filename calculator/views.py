from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты
}


def recipe_view(request, recipe_name):
    recipe = DATA.get(recipe_name)

    if recipe is None:
        return render(request, 'calculator/404.html', status=404)

    # Получаем servings из GET-параметров (по умолчанию 1)
    servings_raw = request.GET.get('servings', 1)

    # Конвертируем в число, обрабатываем ошибки
    try:
        servings = int(servings_raw)
        if servings < 1:
            servings = 1
    except (ValueError, TypeError):
        servings = 1

    # Умножаем каждый ингредиент на количество порций
    recipe_for_servings = {
        ingredient: amount * servings
        for ingredient, amount in recipe.items()
    }

    context = {
        'recipe': recipe_for_servings,
    }

    return render(request, 'calculator/index.html', context)

def index_view(request):
    context = {
        'recipes': DATA.keys(),
    }
    return render(request, 'calculator/index_list.html', context)
