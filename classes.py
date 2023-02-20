"""Demo of classes and objects"""

#"class" holds similar things | "self" is a variable name
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Person: {self.name} | {self.age} years old'
    
    def greet(self):
        print(f'Hello, my name is {self.name} and i am {self.age} old')


class Student(Person):
    def __init__(self, name, age, student_id, grades=None): #"super" just calls the "Person" or the inheritance class
        super().__init__(name, age)

        self.student_id = student_id

        if isinstance(grades, list):
            self.grades = grades
        else:
            self.grades = []

    def __str__(self):
        return f'Student {self.name} | ID: {self.student_id} | {self.get_average()}% average'

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def greet(self):
        print('Im a student')

if __name__ == '__main__':
    my_person = Student("Jero", 23, 301254057)
    my_person.grades.extend([34, 56, 32, 56, 21, 25])

    print(my_person.grades)