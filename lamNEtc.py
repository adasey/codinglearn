# lambda
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'sun']

def change_words(words, func): # 함수를 매개변수로 사용가능
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

#change_words(l, lambda word: word.capitalize())

#hange_words(l, lambda word: word.lower())

# generator
l = ['good morning', 'good evening', 'good afternoon', 'and', 'good night']

def greeting(): # yield : 산출한다.
    yield 'good morning'
    for i in range(10000):
        print(i)
    yield 'good evening'
    yield 'good afternoon'
    yield 'and'
    yield 'good night'

#g = greeting()

#print(next(g)) # 생성된 목록들을 하나하나 출력하나, 그 이상이 호출되면 더 이상 호출 불가
# generator는 각자 개별적인 next의 지정된 포인트가 있어서 개별로 출력 순서가 정해져 있다.
#print(next(g)) # yield 다음에 for 문이 있으면 해당 for문이 전부 완료된 후 다음 yield 문 출력

t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)

r = [i * j for i in t for j in t2]
#print(r)

w = ['mon', 'tue', 'wed']
f = ['coffee', 'water', 'milk']

d = {x: y for x, y in zip(w, f)}
#print(d)

s = set()

s = {i for i in range(10)}
#print(s)

g = (i for i in range(10))

for x in g:
    print(x)