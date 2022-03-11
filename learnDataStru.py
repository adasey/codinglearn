# list
sentence = "my name is john lee"
to_split = sentence.split(' ')
#print(to_split)

merge_as = ' ~ '.join(to_split)
#print(merge_as)

# list copy
# 기존의 x = y식의 리스트 대입은 복사가 아닌 또다른 원본 즉 대입 x의 리스트 값을 바꿔도 y 리스트의 값도 바뀜
x = [1, 2, 3, 4]
y = x.copy()
y = x[:] # 또는 .copy() 처럼 [:]도 가능
y[0] = 50
print("x, y = ", x, ", ", y)

# tuple unpacking
unpack = (10, 20)

x, y = unpack
print(x, y)

a, b = 15, 30 # a = 15, b = 30
a, b = b, a 
print(a, b)

# dictionary
x = {'a' : 1, 'b' : 2}
y = x.copy()
y['a'] = 3
print(x, y)

# set(집합형)
my_friends = {'A', 'B', 'C'}
A_friends = {'B', 'D', 'E', 'F'}

print(my_friends & A_friends)

human = ['apple', 'banana', 'banana', 'pineapple']
kind = set(human)
print(kind)