class Averager():
    def __init__(self):
        self.total = 0
        self.length = 0

    def add_count(self, num):
        self.total = self.total+num
        self.length = self.length + 1

        print(self.total/self.length)

obj1 = Averager()

obj1.add_count(10)
obj1.add_count(20)
