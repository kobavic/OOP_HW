class Student:
    def __init__(self, name: object, surname: object, gender: object) -> object:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

        def rate_lecturer(self, name, surname, course, grade, lecturer=None):
            if isinstance(lecturer,
                          Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    self.grades += {course: grade}
                else:
                    self.grades = {course: grade}
            else:
                return ('Ошибка')

            def __str__(self):
                return f'Имя : {self.name}\n' \
                       f'Фамилия : {self.surname}\n' \
                       f'Средняя оценка за домашние задания: {self.ever_grade()}\n' \
                       f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'


Victor = Student('Victor', 'Kukoba', 'male')
Christina = Student('Christina', 'Smith', 'female')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python', 'Java']


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python', 'Java']
        self.grades = []

    lecturer_attr = {'Phyton': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'Java': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

    def __str__(self):
        return f'Имя : {self.name}\n' \
               f'Фамилия : {self.surname}\n' \
               f'Средняя оценка за лекции: {self.ever_grade()}\n'


Sarah = Lecturer('Sarah', 'Campbel')
Joseph = Lecturer('Joseph', "Seed")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python', 'Java']
        self.grades = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']

    cool_mentor = Mentor('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']

    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_mentor.rate_hw(best_student, 'Python', 10)

    print(best_student.grades)

    def __str__(self):
        return f'Имя : {self.name}\n' \
               f'Фамилия : {self.surname}\n'


Gary = Reviewer('Gary', 'Bonhem')
Emma = Reviewer('Emma', 'Rhodes')


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
