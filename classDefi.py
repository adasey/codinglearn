class Human(object):
    def __init__(self, name = 'tom'): # 생성자
        self.name = name
        print(self.name)

    def say_something(self):
        print(f'I am {self.name}. hello')
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self): # 소멸자 클래스가 사라질 때 발생
        print("good bye")

#person = Human()
#person.say_something()

#del person
import abc

class Person(object):
    def __init__(self, age = 1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception("No drive")

class Adult(Person):
    def __init__(self, age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print("ok")

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model = None):
        self.model = model

    def start_car(self):
        print('run')

    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)

class KiaCar(Car):
    def start_car(self):
        print('faster')

class TeslaCar(Car):
    def __init__(self, model = 'Model S', enable_auto_run = False):
        # self.model = model
        super().__init__(model) # 기반 클래스의 생성자 불러오기.
        self._enable_auto_run = enable_auto_run # 외부에서 사용 불가능하게. 캡슐화, 은닉화.
        # self.__enable_auto_run 만약 __하고 변수로 설정하면 외부에서 호출 아예 불가능, 내부에서만 가능. 캡슐화, 은닉화
        # _ 의 여부에 따라 사용 여부가 갈린다.

    @property # 아래의 함수를 입력하면 외부에서 재설정 불가능
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter # 해당 기능이 존재하면 getter setter의 setter 처럼 작동해 원래대로 기입가능.
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def start_car(self):
        print('fastest')

    def auto_run(self):
        print("Auto Run Start")

tesla_car = TeslaCar('model S')
# print(tesla_car.enable_auto_run)
# tesla_car.enable_auto_run = True

class T(object):
    pass

t = T() # 해당 클래스의 변수가 추가됨.
t.name = 'Mike'
t.age = 20
#print(t.name, t.age)