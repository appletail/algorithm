from datetime import datetime

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod                    # init가 아예 없는 경우에 사용
    def details(cls, name, year):   # 좋은 방법은 아님
        age = datetime.today().year - year
        t = Person()                # t라는 인스턴스 객체 생성
        t.name = name               # 없는거니까 아예 새로 생성
        t.age = age

        return t                    # 인스턴스 개체 t반환

    @classmethod
    def details(cls, name, year):
        age = datetime.today().year - year
        return Person(name, age) #클래스메서드로 인스턴스 만들기
        
    
    def check_age(self):
        if self.age < 19:
            return True
        else:
            return False


p1 = Person('김', )
p2 = Person.details('나', 1994)
p2 = p2.details('박', 1988)

print(p1.name)
print(p1.age)
print(p1.check_age())

print(p2.name)
print(p2.age)
print(p2.check_age())

