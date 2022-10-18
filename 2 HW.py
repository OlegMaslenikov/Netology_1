# Задание 1

user = input("""Вас приветствует ипотечный калькулятор. Необходимо пройти краткий опрос для получения ипотечной ставки
Введите имя: """)

base_percent = 50
child_discount = 0
sal_discount = 0
ins_discount = 0

user1 = input("Вы с Дальнего Востока? Да/Нет: ")
if user1 == "Да":
    base_percent = 2
    print("Ваша ставка:", base_percent, "%")
else:
    with_children = input("У вас в семье более трёх детей? Да/Нет: ")
    sal_project = input("У вас есть зарплатный проект в нашем банке? Да/Нет: ")
    ins_project = input("Хотите ли вы оформить страхование в нашем банке? Да/Нет: ")
    if with_children == "Да":
        base_percent -= 1
    if sal_project == "Да":
        base_percent -= 0.5
    if ins_project == "Да":
        base_percent -= 1.5
    print("Ваша ставка", base_percent, "процента")


# Задание 2

mounth = input("Введите месяц:")
day = int(input("Введите число:"))

if mounth == "Декабрь" and day >= 22 or mounth == "Январь" and day <= 20:
    print("Ваш знак зодиака - Козерог")
elif mounth == "Январь" and day >= 21 or mounth == "Февраль" and day <= 18:
    print("Ваш знак зодиака - Водолей")
elif mounth == "Февраль" and day >= 19 or mounth == "Март" and day <= 20:
    print("Ваш знак зодиака - Рыбы")
elif mounth == "Март" and day >= 21 or mounth == "Апрель" and day <= 20:
    print("Ваш знак зодиака - Овен")
elif mounth == "Апрель" and day >= 21 or mounth == "Май" and day <= 21:
    print("Ваш знак зодиака - Телец")
elif mounth == "Май" and day >= 22 or mounth == "Июнь" and day <= 21:
    print("Ваш знак зодиака - Близнецы")
elif mounth == "Июнь" and day >= 22 or mounth == "Июль" and day <= 22:
    print("Ваш знак зодиака - Рак")
elif mounth == "Июль" and day >= 23 or mounth == "Август" and day <= 23:
    print("Ваш знак зодиака - Лев")
elif mounth == "Август" and day >= 24 or mounth == "Сентябрь" and day <= 22:
    print("Ваш знак зодиака - Дева")
elif mounth == "Сентябрь" and day >= 23 or mounth == "Октябрь" and day <= 23:
    print("Ваш знак зодиака - Весы")
elif mounth == "Октябрь" and day >= 24 or mounth == "Ноябрь" and day <= 22:
    print("Ваш знак зодиака - Скорпион")
elif mounth == "Ноябрь" and day >= 22 or mounth == "Декабрь" and day <= 20:
    print("Ваш знак зодиака - Стрелец")


