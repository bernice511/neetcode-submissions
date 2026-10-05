class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        if not self.min_val or val<=self.min_val[-1]:
            self.min_val.append(val)
        return self.stack.append(val)

        

    def pop(self) -> None:
        last_val = self.stack.pop()
        if last_val == self.min_val[-1]:
            self.min_val.pop()
        return last_val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]
        
