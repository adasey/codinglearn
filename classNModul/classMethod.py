from typing import overload


class Person(object):

    kind = "human"

    def __init__(self, kind):
        self.kind = kind
        self.x = 100

    @classmethod # 해당 선언 시 클래스 메소드로 해당 함수를 개체로 완성되지 않은 b 같은 클래스에서 호출 할 수 있다.
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod # 굳이 이렇게 사용하지 않고 외부에서 사용해도 되기 떄문에 굳이 사용하지 않아도 된다.
    def about(year):
        print(f"about human : {year}")

a = Person("human")
print(a.what_is_your_kind())

b = Person("animal")
print(b.what_is_your_kind())
# print(Person.kind)
# print(Person.what_is_your_kind())

# Person.about(100)
