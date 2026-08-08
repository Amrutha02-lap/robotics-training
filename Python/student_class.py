class Student:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def display(self):
        print("Name:", self.name)
        print("Mark:", self.mark)


student1 = Student("Amrutha", 85)
student1.display()
