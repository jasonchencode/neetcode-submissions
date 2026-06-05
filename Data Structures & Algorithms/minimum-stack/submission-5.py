class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min != None:
            if val <= self.min:
                self.min = val
                self.mins.append(self.min)
        else:
            self.min = val
            self.mins.append(self.min)

    def pop(self) -> None:
        if self.stack[-1] == self.min:
            self.mins.pop(-1)
            if len(self.mins) > 0:
                self.min = self.mins[-1]
            else:
                self.min = None
        self.stack.pop(-1)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
