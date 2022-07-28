class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self): # 일반사용자를 위한 문자열 포맷, 인간친화적
        return f'나는 {self.name} 입니다.'

    def __repr__(self): # 기술자, 개발자를 위한 포맷, 코드 냄새가 나는?
        return f'repr() 호출됨'

    def __add__(self, obj): # p1 + p2
        return self.name + obj.name

p1 = Person('영수')
p2 = Person('영자')

# print(p1)
# print(str(p1)+ '이게 붙네...')
# print(repr(p1))

print(p1 + p2)
