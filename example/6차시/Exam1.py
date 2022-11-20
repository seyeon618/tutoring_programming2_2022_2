class Train:
    def __init__(self, type, fare, start, end):
        self.type = type
        self.amount = fare
        self.start = start
        self.end = end

    def move(self):
        print(self.start, '->', self.end)
        self.start = self.end

    def getOn(self):
        print("탑승 요금: ", self.amount)

    def getOff(self):
        print("출발지: ", self.start)

    def print(self):
        print("기차 종류: ", self.type, "출발지: ", self.start, "도착지: ", self.end, "탑승 요금: ", self.amount)

train = Train("ktx", 25000, "서울역", "용산역")
train.getOn()
train.move()
train.getOff()
train.print()