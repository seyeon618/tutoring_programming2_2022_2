class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def print_avg(self):
        print("name: ", self.name, ", avg: ", self.get_avg())

seyeon = Student("조세연", 100, 85, 60, 80)
seyeon.print_avg()
