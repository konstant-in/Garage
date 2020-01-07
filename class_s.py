"""Определение класса с переменным числом арнументов"""
class Var:
    def __init__(self, **kwargs):
        for attr in kwargs.keys():
            self.__dict__[attr] = kwargs[attr]


v = Var(name="Sam", age=22)
print(v.__dict__)
print(v.name)
print(v.age)

v2 = Var(name="Sam", age=22, x=34)
print(v2.__dict__)
print(v2.name)
print(v2.age)
print(v2.x)
