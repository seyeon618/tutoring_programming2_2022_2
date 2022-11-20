class Human:
    def __init__(self, name, age, sex):
        print("응애응애")
        self.name = name
        self.age = age
        self.sex = sex

    def printName(self):
        print("name: ", self.name)

    def printAge(self):
        print("age: ", self.age)

    def printSex(self):
        print("sex: ", self.sex)

seyeon = Human("조세연", 24, "여")
seyeon.printName()
seyeon.printAge()
seyeon.printSex()
    