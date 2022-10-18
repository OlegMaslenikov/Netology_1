class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        for grades in self.grades.values():
            result = f'\
Имя: {self.name} \n\
Фамилия: {self.surname} \n\
Средняя оценка за курс: {float(sum(grades) / len(grades))} \n\
Курсы в процессе обучения: {self.finished_courses} \n\
Завершенные курсы: {self.courses_in_progress}'
            return result

    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector,
                      Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        for grades in self.grades.values():
            result = \
f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {float(sum(grades) / len(grades))}"""
        return result



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = \
f"""Имя: {self.name}
Фамилия: {self.surname}"""
        return result


reviewer1 = Reviewer("Petya", "Peroy")
lec1 = Lecturer("Drow", "Ranger")
lec1.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']

reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
reviewer1.rate_hw(best_student, 'Python', 10)
best_student.rate_lecturer(lec1, 'Python', 10)

print(reviewer1)
