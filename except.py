# __ 에 있는 변수 값이 있기 때문에, 이해하고 사용하지 않으면 심각할 수도 있다.
"""
TEST
"""
animal = 'cat'

def f():
    # global animal # 글로벌 변수를 함수에서 사용하려고 할 때
    #print(animal) # 지금 상태에서는 글로벌 상태의 변수를 local에서 호출은 어렵다. 에러발생 위의 global로 선언하면 사용가능.
    animal = 'dog'
    print("lo", locals()) # local변수로 선언된 목록 출력

def c():
    """함수 설명"""
    print(c.__name__)
    print(c.__doc__)

#f()
# print("gl", globals()) globals 변수로 선언된 모든 목록 출력

#c()

l = [1, 2, 3]
i = 5

#try:
#    l[0]

#except IndexError as ex: # index Error 가 발생 시에만, 특정 에러가 발생 시에만 설정 가능
#    print(f"Don't Worry : {ex}")

#except NameError as ex:
#    print(ex)

#except Exception as ex:
#    print(f"what's wrong? : {ex}")

#else: # 실행이 정상적으로 실행되면 이 else가 실행됨.
#    print('done')

#finally: # 반드시 except 실행이 끝난 뒤 실행됨. except 문이 없더라도 에러 메시지 전에 실행됨.
#    print('clean up')

# 예외 작성
# raise IndexError('test error') # error 실행

class UppercaseError(Exception):
    pass

def check():
    words = ['Apple', 'Orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()

except UppercaseError as exc:
    print('This is my fault. go next')
