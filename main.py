class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __average_rating(self):
        rate_sum = 0
        leng = 0
        for course, rate in self.grades.items():
            rate_sum += sum(rate)
            leng += len(rate)
        if leng != 0:
            return rate_sum / leng
        return 0


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.__average_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Нет такого студента!'
        return self.__average_rating() < other.__average_rating()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)

    def __average_rating(self):
        rate_sum = 0
        leng = 0
        for course, rate in self.grades.items():
            rate_sum += sum(rate)
            leng += len(rate)
        if leng != 0:
            return rate_sum / leng
        return 0

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции:{self.__average_rating()}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Нет такого лектора!'
        return self.__average_rating() < other.__average_rating()



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        pass


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res


def all_students_average_rate(students_list, course_name):
    i = 0
    rate = 0
    for student in students_list:
        if isinstance(student, Student):
            rate += sum(student.grades[course_name])
            i += 1
    if i != 0:
        return f'Средняя оценка за ДЗ для студентов курса {course_name}: {rate / i}'
    return 'Ошибка'

def all_lecturer_average_rate(lecturer_list, course_name1):
    i = 0
    rate = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer):
            rate += sum(lecturer.grades[course_name1])
            i += 1
    if i != 0:
        return f'Средняя оценка лекторов за курс {course_name1}: {rate / i}'
    return 'Ошибка'



student1 = Student('Ivan', 'Ivanov', 'M')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.courses_in_progress += ['C++']

student1.add_courses('C')
student1.add_courses('Java')

student2 = Student('Ivanka', 'Trump', 'F')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.courses_in_progress += ['C++']

student2.add_courses('Rust')
student2.add_courses('Go')


reviewer1 = Reviewer('Donald', 'Trump')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['C++']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('', 'Putin')
reviewer2.courses_attached += ['C++']
reviewer2.courses_attached += ['Git']
reviewer2.courses_attached += ['Python']


lecturer1 = Lecturer('Emmanuel', 'Makron')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['C++']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Joe', 'Biden')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['C++']
lecturer2.courses_attached += ['Git']


student1.rate_hw(lecturer1, 'Python', 3)
student1.rate_hw(lecturer1, 'C++', 1)
student1.rate_hw(lecturer1, 'Git', 2)
student1.rate_hw(lecturer2, 'Python', 8)
student1.rate_hw(lecturer2, 'C++', 10)
student1.rate_hw(lecturer2, 'Git', 5)

student2.rate_hw(lecturer1, 'Python', 10)
student2.rate_hw(lecturer1, 'C++', 4)
student2.rate_hw(lecturer1, 'Git', 1)
student2.rate_hw(lecturer2, 'Python', 8)
student2.rate_hw(lecturer2, 'C++', 5)
student2.rate_hw(lecturer2, 'Git', 2)


reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'C++', 2)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'C++', 5)
reviewer1.rate_hw(student2, 'Git', 10)

reviewer2.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'C++', 2)
reviewer2.rate_hw(student1, 'Git', 1)
reviewer2.rate_hw(student2, 'Python', 3)
reviewer2.rate_hw(student2, 'C++', 1)
reviewer2.rate_hw(student2, 'Git', 8)



print('Студенты--------')
print(student1)
print(student2)
print('Ревьюеры--------')
print(reviewer1)
print(reviewer1.courses_attached)
print(reviewer2)
print(reviewer2.courses_attached)
print('Лекторы---------')
print(lecturer1)
print(lecturer1.grades)
print(lecturer2)
print(lecturer2.grades)
print('Оценки студентов--')
print(student1.grades)
print(student2.grades)
print('Сравнение--------')
print(student1 < student2)
print(lecturer1 > lecturer2)
print('Функции----------')

students_list = [student1, student2]
course_name = 'Git'
lecturer_list = [lecturer1, lecturer2]
course_name1 = 'C++'

print(all_students_average_rate(students_list, course_name))
print(all_lecturer_average_rate(lecturer_list, course_name1))



