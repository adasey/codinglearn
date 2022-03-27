# 클로져
# def base(x):
#     def plus(y):
#         return x + y
#     return plus

# plus = base(10) # y 값
# print(plus(10)) # x 값
# print(plus(30))
# 아래의 기능에서는 해당 함수의 글로벌 변수가 변경될 수 있으나 위의 함수에서는 함부로 수정이 불가능하다.
# i = 0
# def add_num():
#     def plus(y):
#         return i + y
#     return plus

# i = 10
# plus = add_num()
# print(plus(10))
# i = 100
# print(plus(20))

# from roboter import robotControll
# 
# class MainError(Exception):
    # pass
# 
# def main():
    # start = robotControll.Conversation()
    # start.TalkAboutRestaurant()
    # raise MainError
# 
# x = [(i, x, y) for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]] # 피하는게 좋다.
# 
# d = {'key': 'val1', 'key2': 'val2'}
# 
# if 'key' in d:
    # print('test')

# if 'key' in d.keys(): 불필요한 .key() 호출
    # print("test")

# for key, val in d.items(): # 변수명의 명칭을 의미있는 단어로 부여할 것. k나 v 등은 사용은 쉬우나 이해가 힘들다.
#     print(key, val)

# if __name__ == '__main__':
#     main()

# genarator
# def t():
    # num = []
    # for i in range(10):
        # yield i generator 시 yield 사용
        # num.append(i)
    # return num

# for i in t():
    # print(i)

# def other_func(f):
#     print(f(10))

# def test_func(x):
#     return x * 2

# def test_func2(x):
#     return x * 5

# other_func(test_func)
# other_func(test_func2)
# other_func(lambda x: x * 2)
# other_func(lambda x: x * 5)

# y = None
# x = 1 if not y else 2
# print(x)