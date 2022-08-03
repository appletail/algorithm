import random

class pair():

    def __init__(self, lst):
        self.lst = lst

    def pick(self, n):
        return random.sample(self.lst, n)

    def match_pair(self):
        match = []
        tmp = []
        if len(self.lst) % 2 == 1:
            tmp.append(random.sample(self.lst, 3))
            for i in tmp[0]:
                self.lst.remove(i)
            match.append(tmp.pop(0))
             

            for _ in range(int(len(self.lst)/2)):
                tmp.append(random.sample(self.lst, 2))
                for i in tmp[0]:
                    self.lst.remove(i)
                match.append(tmp.pop(0))
            
            return match


        else:
            for _ in range(int(len(self.lst)/2)):
                tmp.append(random.sample(self.lst, 2))
                for i in tmp[0]:
                    self.lst.remove(i)
                match.append(tmp.pop(0))
            
            return match
            

students = ['김', '나', '박', '이', '심', '최', '강', '구', '노', '임', '여']

pair_matching = pair(students)

print(pair_matching.pick(2))
print(pair_matching.match_pair())