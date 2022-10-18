# Задание 1
#
# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]
# new_voc = {}
#
# for voc in geo_logs:
#     # print(wok)
#     for key, value in voc.items():
#         # print(key, value)
#         for item in value:
#             # print(item)
#             if item == "Россия":
#                 new_voc[key] = value
#
# print(new_wok)


# Задание 2
#
# new_list = []
# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
# for number in ids.values():
#     # print(number)
#     for item in number:
#         new_list.append(item)
# # print(new_list)
# a = set(new_list)
# print(a)


# Задание 3
#
# queries = [
#     'смотреть сериалы онлайн',
#     'новости спорта',
#     'афиша кино',
#     'курс доллара',
#     'сериалы этим летом',
#     'курс по питону',
#     'сериалы про спорт'
# ]
#
# total_searches = len(queries)
# freqs = {}
#
# for q in queries:
#     wlen = q.count(" ") + 1
#     # wlen = len(q.split(" "))
#     print(wlen)
#     if wlen == (q.count(" ") + 1):
#         freqs[wlen] = wlen + 1
#
# print(freqs)
# for words, numbers in freqs.items():
#   print(f'Поисковых запросов из {words} слов(а) {int(numbers / total_searches * 100)}%')


# Задание 4
#
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
#
# max_count = 0
# max_id = None
# count = (list(stats.values()))
#
# for id, number in enumerate(count):
#   if number > max_count:
#     max_count = number
#     max_id = id
#
# print(f'Больше всего объёма у {list(stats)[max_id].capitalize()}, {max_count}')