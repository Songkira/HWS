# from datetime import datetime
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     @classmethod
#     def details(cls, name, year):
#         age = datetime.today().year -year
#         name = name
#         return Person(name , age)

#     def check_age(self):
#         if self.age <= 19:
#             return False
#         else:
#             return True
        
        
# p1 = Person('진이', 19)
# p2 = Person.details('수미', 2003)
# print(p1.check_age())
# print(p2.check_age())
# #---------------------------
# class PublicTransport:
#     customer = 0
#     def __init__(self, name, fare):
#         self.name = name
#         self.fare = fare
#         # fare 는 합계 // 탑승객수
#         self.fare += self.fare
        
    
#     def get_in(self):
#         PublicTransport.customer += 1
#         return PublicTransport.customer

#     def get_off(self):
#         PublicTransport.customer -= 1
#         return PublicTransport.customer

#     def profit(self):
#         return self.fare * PublicTransport.customer

# p1 = PublicTransport('주하', 1000)
# p2 = PublicTransport('하늘', 1000)
# p3 = PublicTransport('진희', 500)
# p4 = PublicTransport('근태', 1000)
# print(p1.get_in())
# print(p1.profit())

# print(p2.get_in())
# print(p2.profit())

# print(p3.get_in())
# print(p3.profit())

# print(p4.get_off())
# print(p4.profit())
# ------------------------------------
# 추가 지식
# from datetime import datetime

# cur_time = datetime(year=2022,month=7,day = 28 )

# print(str(cur_time))
# print(repr(cur_time))

# #2022-07-28 00:00:00
# # datetime.datetime(2022, 7, 28, 0, 0)
# -------------------------------------- -------
# 클래스 메소드를 팩토리 메소드로 활용  # 데일리 실습 8-2 참조
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def check_age(self): # 로컬변수 임. 함수 종료하면 사라짐.
        name = self.name

    @classmethod
    def details(cls,name, age): # name, age는 매개변수
        return Person(name, age) # cls(name, age)

    # def __str__(self):
        # return f'{self.name}는 {self.age}살'

    def 
p1 = Person('영수', 27)
p2 = Person.details('영희', 28)
print(p1)
print(p2)