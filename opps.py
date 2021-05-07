class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        print(self.grade)
class Course:
    def __init__(self, course, max_student):
        self.course = course
        self.max_student = max_student
        self.student = []
    def printStudent(self, student):
        if len(self.student) < self.max_student:
            self.student.append(student)
            return True
        return False

s1 = Student("Ashish", 21, "Very Good")
s2 = Student("Ankit", 26, "ok")

course = Course("Science", 2)

course.printStudent(s1)
course.printStudent(s2)

print(course.student[0].name)