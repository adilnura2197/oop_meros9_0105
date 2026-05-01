class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def teach(self):
        print(f"{self.name}")


class MathTeacher(Teacher):
    def __init__(self, name, subject, experience, level, salary):
        super().__init__(name, subject, experience)
        self.level = level
        self.salary = salary

    def teach(self):
        super().teach()
        print(f"Level: {self.level}")


m1 = MathTeacher("Ali", "dunyo", "Tajribali", "2", 200000)
m1.teach()
