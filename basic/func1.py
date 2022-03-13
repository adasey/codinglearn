#function def : 정의하다
def say_hello():
    var1 = 'hello'
    return var1

var = say_hello()

def say_color():
    print("blue")

s = say_color

#print(var)
#s() # 함수를 아무 변수에 넣고 변수() 를 입력하면 함수 호출 가능

# 반환값 선언
num: int = 10

def add_num(a:int, b:int) -> int:
    return a + b

r = add_num(10, 20)
#print(r)

# 인수
def menu(entree='steak', drink='wine', dessert='cookie'):
    print(entree, ',', drink, ',', dessert)

#menu()
#menu('beef', dessert = 'icecream', drink = 'beer') # 매개변수를 생략해도 되나, 명시해도 됨. 순서를 바꾸어 쓰더라도 명시가 되어 있으면 정상적으로 작동
# 순서대로라면 첫번째 변수가 명시가 생략되도 정상적으로 진행됨. 그러나 순서가 바뀐 상태면 바뀐 명시부터 생략하면 오류가 발생함.
# 초기 변수를 정해놓으면 아무것도 명시하지 않아도 함수 호출 가능

# default 인수 유의점
def test_func(x, l=None): # l이 None 일 경우는 빈리스트로 함수 내에서 초기화 해줌
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
#print(r)
# 파이썬에서는 리스트는 참조반환 되므로 초기 변수 설정으로 list 를 빈 리스트로 하지 않아도 됨. 
# 처음만 빈 리스트로 정하고 그 뒤로는 그 리스트의 주소를 참조하기 때문에 기존 리스트에 추가됨.

# 위치 인수 튜플화
def say_something(word, *args): # 굳이 args가 아니여도 되나, *을 붙이고 사용하면 tuple로 합쳐주는듯
    print(word)
    for arg in args:
        print(arg)

t = ('Mike', 'Nance', 'Jain')
#say_something('hi', *t) # 이런식으로 쓰긴 한다. 핵심은 *args

# 키워드 인수
def menu_list1(**kwargs): # ** 두개의 매개변수는 dic형
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

d = {'entree':'beef', 'drink':'iceamericano','dessert':'icecream'}

menu_list1(**d) # tuple 때처럼 사전형 사용 시 ** 붙이면 됨.

def menu_list(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu_list('banana', 'apple', 'orange', entree='beef', drink='coffee') # 요것도 순서 주의 이것처럼 입력 시 사과 오렌지는 튜플로, 
# 뒤의 변수는 dic 으로 entree : beef , drink : coffee로 dic 형태로 묶인다.
