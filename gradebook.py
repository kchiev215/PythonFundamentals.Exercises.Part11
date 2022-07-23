from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, alive):
        self.alive = alive


class Instructor(Person):
    def __init__(self, first_name, last_name, dob):
        self.instructor_id = f'instructor_{uuid4()}'
        super().__init__(first_name, last_name, dob)


class Student(Person):
    def __init__(self, first_name, last_name, dob):
        self.student_id = f'student_{uuid4()}'
        super().__init__(first_name, last_name, dob)


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)


class College(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)


class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors.append(f'Student: {instructor.first_name} {instructor.last_name} {instructor.dob}, '
                               f'{instructor.instructor_id}')
        return self.instructors

    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)
        return self.instructors

    def add_student(self, student):
        self.students.append(f'Student: {student.first_name} {student.last_name} {student.dob}, {student.student_id}')
        return self.students

    def print_instructors(self):
        print(f'{self.instructors}')

    def print_students(self):
        print(f'{self.students}')

#
# zipcoder = ZipCodeStudent("Fitru", "Fitru", "07/01/22")
# classroom = Classroom()
# classroom.add_student(zipcoder)
# print(classroom.print_students())
# zipcoder.update_first_name("Jeffy")
# print(zipcoder.first_name)

