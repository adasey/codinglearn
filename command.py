from re import U
import sys

for i in sys.argv:
    print(i)


# import
# import packages.utils
from packages.tools import utils# as u
# from packages.utils import say_twice

#함수 중복 선언 시 마지막 방법은 함수의 충돌이 일어남.

#r = utils.say_twice("hello")

#print(r)

# import2
# from packages.talk import human
# from packages.talk import animal
#from packages.talk import * # 특정 모듈이 아닌 알 수 없는 모듈이 호출될 뜻이라는 것으로 추천은 하지 않음. __all__에서 확인이 가능하더라도.

#print(animal.cry())
#print(human.cry())

try:
    from packages import utils
except ImportError:
    from packages.tools import utils

print(utils.say_twice('word'))

