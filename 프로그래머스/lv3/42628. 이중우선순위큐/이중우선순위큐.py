from heapq import heapify, heappush, heappop

class DoubleHeap:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.isDeleted = [0] * 1_000_001
        self.length = 0
        
    def insertNum(self, num, idx):
        heappush(self.min_heap, (num, idx))
        heappush(self.max_heap, (-num, idx))
        self.length += 1
    
    def popNum(self, num):
        if self.length == 0:
            return
        result = 0
        
        if num == 1:
            popedNum, idx = heappop(self.max_heap)
            while self.isDeleted[idx]:
                popedNum, idx = heappop(self.max_heap)
            result = -popedNum
        else:
            popedNum, idx = heappop(self.min_heap)
            while self.isDeleted[idx]:
                popedNum, idx = heappop(self.min_heap)
            result = popedNum
            
        self.isDeleted[idx] = 1
        self.length -= 1
        
        return result
        
    
    def printMinMax(self):
        if self.length == 0:
            return [0, 0]
        else:
            return [self.popNum(1), self.popNum(-1)]
            
    
    
    def act(self, operation, idx):
        order, num = operation.split(' ')
        num = int(num)
        if order == 'I':
            self.insertNum(num, idx)
        elif order == 'D':
            self.popNum(num)
                
    
def solution(operations):
    heap = DoubleHeap()
    
    for i in range(len(operations)):
        heap.act(operations[i], i)
    
    
    return heap.printMinMax()
