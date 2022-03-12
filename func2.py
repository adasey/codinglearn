# 함수 help doc
def example_func(param1, param2):
    """Example function with types documented in the docstirng.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parametre.

    Returns:
        bool: The return value. True for success, False otherwise
    """

    print(param1)
    print(param2)
    return True

#help(example_func.__doc__)

# 함수 내 함수
def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

#outer(1, 2)


# clouser
def outer(a, b):

    def inner():
        return a+b

    return inner

# print(outer(1, 2)) # 해당 함수의 오브젝트가 출력

f = outer(1, 2) # 함수의 더한 값의 함수가 들어감.
r = f() # f()를 통해 변수를 실행하면 inner 함수가 실행된 결과가 들어감.
#print(r) # 3출력

# 사용하는 경우는 보통 함수의 기능을 바로 사용하지 않고 추후 사용을 원할 시 clouser 사용정도로

def circle_area_func(pi):
    
    def circle_area(radius):
        return pi * radius ** 2

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

#print(ca1(10))
#print(ca2(10))

# decorator : 함수의 호출 전 호출 후 특정 기능을 사용하고 싶다면 사용.
def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print("func:", func.__name__)
        print("args:", args)
        print('kwargs:',kwargs)
        result = func(*args, **kwargs)
        print("result:", result)
        return result
    return wrapper

@print_info # at mark 를 이용하면 알아서 바로 inner 함수를 호출 - add_num이 wrapper로
@print_more # 위에서 아래 순서로 함수에 대입됨.
def add_num(a, b):
    return a + b

r = add_num(10, 20) # 결과는 바로 r로
print(r)
