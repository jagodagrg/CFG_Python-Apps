import requests

api_key = '627b5f85bc7f469ca36310dc995c608f'


def call_search_api(ingredient):
    url = 'https://api.spoonacular.com/recipes/findByIngredients?apiKey={}&ingredients={}'.format(api_key, ingredient)
    response = requests.get(url)
    recipes = response.json()
    return recipes


def call_recipe_details_api(recipe_id):
    url = 'https://api.spoonacular.com/recipes/{}/information?apiKey={}&includeNutrition=false'.format(recipe_id, api_key)
    response = requests.get(url)
    recipe = response.json()
    return recipe


def run():
    ingredient = input('What ingredient would you like to use today? ')
    is_vegan = input('Would you like to see only vegan recipes? (y/n) ')
    results = call_search_api(ingredient)
    print('\nHere are your options:\n')

    for result in results:
        recipe_id = result['id']
        selected_recipe = call_recipe_details_api(recipe_id)

        if is_vegan == 'n' or (is_vegan == 'y' and selected_recipe['vegan'] is True):
            print(selected_recipe['title'])
            print(selected_recipe['sourceUrl'])
            print('\n')

    print('\nEnjoy!\n')


run()
