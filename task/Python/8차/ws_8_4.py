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

class Bus(PublicTransport):
    
    def __init__(self, name, fare, ride_num):
        super().__init__(name, fare)
        self.ride_num = ride_num

    def get_in(self, num):
        if num > (self.ride_num - self.passenger):
            self.passenger = self.ride_num
            return print('더이상 탑승할 수 없습니다.')
        else:
            return super().get_in(num)


b = Bus('bus', 500, 40)

b.get_in(38)
b.get_in(3)
print(b.passenger)
print(b.profit())