class Server:
    k, time = 0, 0

    def __init__(self, k):
        self.k = k
        
    def check(self):
        if self.k == self.time:
            return False
        return True
    
    def increase(self):
        self.time += 1
        
        
def solution(players, m, k):
    answer = 0
    servers = {}
    possible = m-1
    for time, player in enumerate(players):
        while possible < player:
            answer += 1
            servers[answer] = Server(k)
            possible += m

        returnServer = []
        for key, value in servers.items():
            value.increase()
            if not value.check():
                returnServer.append(key)
        for server in returnServer:
            del servers[server]
            possible -= m

    return answer
