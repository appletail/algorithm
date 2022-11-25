class PublicTransport:

    def __init__(self, name, fare):
        self.passenger = 0
        self.name = name
        self.fare = fare
    def get_in(self, num):
        self.passenger += num
    def get_off(self, num):
        self.passenger -= num
    
    def profit(self):
        return self.fare * self.passenger

a = PublicTransport('subway', 1000)
b = PublicTransport('bus', 500)

a.get_in(500)
a.get_off(5)
print(a.passenger)
print(a.profit())

b.get_in(1800)
b.get_off(56)
print(b.passenger)
print(b.profit())