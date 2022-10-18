from pprint import pprint
# cook_book = {}
#
# with open('recipes.txt', encoding='utf-8') as f:
#     for line in f:
#         dish_name = (line.strip())
#         ingredients_quantity = (f.readline().strip())
#         ingredients_list = []
#         for ingr in range(int(ingredients_quantity)):
#             ingredients_dict = {}
#             ingredient_name, quantity, measure = f.readline().split('|')
#             ingredients_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
#         cook_book[dish_name] = ingredients_list
#         f.readline()
    # pprint(cook_book)

with open ('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = (line.strip())
        ingredients_quantity = (file.readline().strip())
        ingredients_list = []
        for ingrts in range(int(ingredients_quantity)):
            ingredients_dict = {}
            ingredient_name, quantity, measure = file.readline().split('|')
            ingredients_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book[dish_name] = ingredients_list



def dishes_list (dishes, person_count):
    info_ingredients_dict = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            result = 'Такого блюда в книге нет!'
            return result
        else:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                amount = int(ingredient['quantity']) * person_count
                un = ingredient['measure']
                name = ingredient['ingredient_name']
                if name not in info_ingredients_dict:
                    info_ingredients_dict[name] = {'measure': un, 'quantity': amount}
                else:
                    info_ingredients_dict[name]['quantity'] += amount
    pprint(info_ingredients_dict)


dishes_list (['Запеченный картофель', 'Омлет'], 10)


