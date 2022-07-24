import unittest
import unittest.mock
import gradebook


class TestString(unittest.TestCase):

    def test_update_first_name(self):
        person1 = gradebook.Person("Jerry", "Jeff", "07221993")
        person1.update_first_name("Sarah")
        expected = person1.first_name
        self.assertEqual(expected, "Sarah")

    def test_update_first_name1(self):
        person1 = gradebook.Person("Sarah", "Jeff", "07221993")
        person1.update_first_name("Violet")
        expected = person1.first_name
        self.assertEqual(expected, "Violet")

    def test_update_first_name2(self):
        person1 = gradebook.Person("Zach", "Jeff", "07221993")
        person1.update_first_name("York")
        expected = person1.first_name
        self.assertEqual(expected, "York")

    def test_update_first_name3(self):
        person1 = gradebook.Person("Lam", "Jeff", "07221993")
        person1.update_first_name("Louis")
        expected = person1.first_name
        self.assertEqual(expected, "Louis")

    def test_update_first_name4(self):
        person1 = gradebook.Person("Troy", "Jeff", "07221993")
        person1.update_first_name("Lousy")
        expected = person1.first_name
        self.assertEqual(expected, "Lousy")

    def test_update_first_name5(self):
        person1 = gradebook.Person("Ervin", "Jeff", "07221993")
        person1.update_first_name("Ewing")
        expected = person1.first_name
        self.assertEqual(expected, "Ewing")

    def test_update_first_name6(self):
        person1 = gradebook.Person("Zarah", "Jeff", "07221993")
        person1.update_first_name("Philip")
        expected = person1.first_name
        self.assertEqual(expected, "Philip")

    def test_update_first_name7(self):
        person1 = gradebook.Person("Yordle", "Jeff", "07221993")
        person1.update_first_name("Yankee")
        expected = person1.first_name
        self.assertEqual(expected, "Yankee")

    def test_update_last_name(self):
        person1 = gradebook.Person("Yordle", "Jeff", "07221993")
        person1.update_last_name("Yankee")
        expected = person1.last_name
        self.assertEqual(expected, "Yankee")

    def test_update_last_name1(self):
        person1 = gradebook.Person("Steve", "Jobs", "07221993")
        person1.update_last_name("Landy")
        expected = person1.last_name
        self.assertEqual(expected, "Landy")

    def test_update_last_name2(self):
        person1 = gradebook.Person("Yordle", "Philip", "07221993")
        person1.update_last_name("Tum")
        expected = person1.last_name
        self.assertEqual(expected, "Tum")

    def test_update_last_name3(self):
        person1 = gradebook.Person("Phil", "Ervie", "07221993")
        person1.update_last_name("Frank")
        expected = person1.last_name
        self.assertEqual(expected, "Frank")

    def test_update_last_name4(self):
        person1 = gradebook.Person("Leap", "Yesh", "07221993")
        person1.update_last_name("Yush")
        expected = person1.last_name
        self.assertEqual(expected, "Yush")

    def test_update_last_name5(self):
        person1 = gradebook.Person("Kev", "Yuno", "07221993")
        person1.update_last_name("Yevin")
        expected = person1.last_name
        self.assertEqual(expected, "Yevin")

    def test_update_last_name6(self):
        person1 = gradebook.Person("Plih", "Ploh", "07221993")
        person1.update_last_name("Ervin")
        expected = person1.last_name
        self.assertEqual(expected, "Ervin")

    def test_update_last_name7(self):
        person1 = gradebook.Person("Ash", "Meh", "07221993")
        person1.update_last_name("Yum")
        expected = person1.last_name
        self.assertEqual(expected, "Yum")

    def test_update_dob(self):
        person1 = gradebook.Person("Ash", "Meh", "07221993")
        person1.update_dob("02221993")
        expected = person1.dob
        self.assertEqual(expected, "02221993")

    def test_update_dob1(self):
        person1 = gradebook.Person("Ash", "Meh", "07221993")
        person1.update_dob("01111111")
        expected = person1.dob
        self.assertEqual(expected, "01111111")

    def test_update_dob2(self):
        person1 = gradebook.Person("Ash", "Bleh", "03122900")
        person1.update_dob("02222222")
        expected = person1.dob
        self.assertEqual(expected, "02222222")

    def test_update_dob3(self):
        person1 = gradebook.Person("Ash", "Yum", "03051991")
        person1.update_dob("03051996")
        expected = person1.dob
        self.assertEqual(expected, "03051996")

    def test_update_dob4(self):
        person1 = gradebook.Person("Ash", "Yum", "02222222")
        person1.update_dob("03122900")
        expected = person1.dob
        self.assertEqual(expected, "03122900")

    def test_update_dob5(self):
        person1 = gradebook.Person("Tyler", "Yum", "02222222")
        person1.update_dob("09231993")
        expected = person1.dob
        self.assertEqual(expected, "09231993")

    def test_add_instructor(self):
        instructor1 = gradebook.Instructor("Lloyd", "Perez", "07012022")
        expected = gradebook.Classroom().add_instructor(instructor1)
        result = gradebook.Classroom().print_instructors()
        self.assertEqual(expected, result)

    def test_add_instructor1(self):
        instructor1 = gradebook.Instructor("Tenae", "Tenae", "07012021")
        expected = gradebook.Classroom().add_instructor(instructor1)
        result = gradebook.Classroom().print_instructors()
        self.assertEqual(expected, result)

    def test_add_instructor3(self):
        instructor1 = gradebook.Instructor("Nicholas", "Olas", "07012010")
        expected = gradebook.Classroom().add_instructor(instructor1)
        result = gradebook.Classroom().print_instructors()
        self.assertEqual(expected, result)

    def test_add_instructor4(self):
        instructor1 = gradebook.Instructor("Kris", "Younger", "01111111")
        expected = gradebook.Classroom().add_instructor(instructor1)
        result = gradebook.Classroom().print_instructors()
        self.assertEqual(expected, result)

    def test_add_instructor5(self):
        instructor1 = gradebook.Instructor("Thina", "Chiev", "07221993")
        expected = gradebook.Classroom().add_instructor(instructor1)
        result = gradebook.Classroom().print_instructors()
        self.assertEqual(expected, result)

    def test_add_student(self):
        student = gradebook.Student("Nicholas", "Olas", "04031993")
        expected = gradebook.Classroom().add_student(student)
        result = gradebook.Classroom().print_students()
        self.assertEqual(expected, result)

    def test_add_student1(self):
        student = gradebook.Student("Thina", "Chiev", "07221993")
        expected = gradebook.Classroom().add_student(student)
        result = gradebook.Classroom().print_students()
        self.assertEqual(expected, result)

    def test_add_student3(self):
        student = gradebook.Student("Effy", "Jiffy", "01223333")
        expected = gradebook.Classroom().add_student(student)
        result = gradebook.Classroom().print_students()
        self.assertEqual(expected, result)

    def test_add_student4(self):
        student = gradebook.Student("Luffy", "Liffy", "05662102")
        expected = gradebook.Classroom().add_student(student)
        result = gradebook.Classroom().print_students()
        self.assertEqual(expected, result)

    def test_add_student5(self):
        student = gradebook.Student("Zorra", "Zirro", "06021985")
        expected = gradebook.Classroom().add_student(student)
        result = gradebook.Classroom().print_students()
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()

