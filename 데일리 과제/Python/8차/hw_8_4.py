class Stack:
    def __init__(self):
        self.lst = []

    def empty(self):
        if self.lst == []:
            return True
        else:
            return False

    def top(self):
        if Stack.empty(self) == True:
            return
        else:
           return self.lst[-1]
    
    def pop(self):
        tmp = self.lst[-1]
        del self.lst[-1]
        return tmp

    def push(self, lst_value):
        self.lst.append(lst_value)
    
    def __repr__(self):
        return repr(self.lst)


a = Stack()
a.push('a')
a.push('b')

print(a.top())
print(a.pop())
print(a.top())

print(a.__repr__())