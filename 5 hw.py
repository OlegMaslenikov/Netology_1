documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.


def people (doc_number):
    for vocs in documents:
        # print(vocs)
        for key, value in vocs.items():
            if doc_number == value:
                print(vocs["name"])


def shelf (doc_number):
    for key, value in directories.items():
        for item in value:
            if doc_number == item:
                print(key)
                break
        else:
            print("Такого документа нет!")
        return


def list ():
    for vocs in documents:
        print(f' {vocs["type"]} "{vocs["number"]}" "{vocs["name"]}"')


def add (type, number, name, shelf):
    if int(shelf) > 3 or int(shelf) < 1:
        print("Такой полки нет!")
    else:
        new_voc = {"type": type, "number": number, "name": name}
        documents.append(new_voc)
        for key, value in directories.items():
            if shelf == key:
                value.extend(number)
        print("Данные добавлены")


while True:
    user_command = input("Введите команду: ")
    if user_command == "p":
        doc_number = input("Какой номер документа: ")
        people(doc_number)
    elif user_command == "s":
        doc_number = input("Какой номер документа: ")
        str(shelf(doc_number))
    elif user_command == "l":
        list()
    elif user_command == "a":
        type = input("Какой тип документа: ")
        number = input("Какой номер документа: ")
        name = input("Имя владельца: ")
        shelf = input("Номер полки: ")
        add(type, number, name, shelf)
    else:
        print("Повторите попытку")

