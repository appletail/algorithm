class Tired:
    def __init__(self, k, dungeons):
        self.k = k
        self.dungeons = dungeons
        self.N = len(dungeons)
        self.used = [0] * len(dungeons)
        self.answer = 0
        self.minK = min(dungeons)[0]

    def adventure(self, depth, curS):
        if (self.N - depth + curS) <= self.answer:
            return
        
        if self.N == depth or self.k < self.minK:
            self.answer = max(curS, self.answer)
            return
        
        for i in range(self.N):
            if not self.used[i]:
                self.used[i] = 1
                self.adventure(depth + 1, curS)
                if self.k >= self.dungeons[i][0]:
                    self.k -= self.dungeons[i][1]
                    self.adventure(depth + 1, curS + 1)
                    self.k += self.dungeons[i][1]
                self.used[i] = 0
    
    def result(self):
        return self.answer
    
    
def solution(k, dungeons):
    fighter = Tired(k, dungeons)
    fighter.adventure(0, 0)
    
    return fighter.result() if fighter.result() else -1