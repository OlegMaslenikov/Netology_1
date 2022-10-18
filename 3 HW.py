# # Задание 1
#
# # boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# # girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# # new_turple_b = sorted(boys)
# # new_turple_g= sorted(girls)
# # couple = list(zip(new_turple_b,new_turple_g))
# # print("Идеальные пары: ")
# # for b, g in couple:
# #     print (f" {b} и {g}")
#
# # Задание 2
# person = 5
# cook_book = [
#   ['салат',
#       [
#         ['картофель', 100, 'гр.'],
#         ['морковь', 50, 'гр.'],
#         ['огурцы', 50, 'гр.'],
#         ['горошек', 30, 'гр.'],
#         ['майонез', 70, 'мл.'],
#       ]
#   ],
#   ['пицца',
#       [
#         ['сыр', 50, 'гр.'],
#         ['томаты', 50, 'гр.'],
#         ['тесто', 100, 'гр.'],
#         ['бекон', 30, 'гр.'],
#         ['колбаса', 30, 'гр.'],
#         ['грибы', 20, 'гр.'],
#       ],
#   ],
#   ['фруктовый десерт',
#       [
#         ['хурма', 60, 'гр.'],
#         ['киви', 60, 'гр.'],
#         ['творог', 60, 'гр.'],
#         ['сахар', 10, 'гр.'],
#         ['мед', 50, 'мл.'],
#       ]
#   ]
# ]
# for receipt, list in cook_book:
#     print()
#     print(f"{receipt.capitalize ()}:")
#     for ingredients, weight, g in list:
#         print(ingredients, str(weight * person)+g)