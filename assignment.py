class MaxSizeList():
    def __init__(self, max):
        self.max = max
        self.num =[]

    def push(self, val):
        self.num.append(val)
        if len(self.num) > self.max:
            self.num.pop(0)
    def show(self):
        return self.num

maxsizelist = MaxSizeList(3)
maxsizelist.push(1)
maxsizelist.push(2)
maxsizelist.push(3)
maxsizelist.push(4)
maxsizelist.push(5)
print(maxsizelist.show())
