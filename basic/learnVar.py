s = "hello i am steve"

is_start = s.startswith('hello')

print(is_start)

print(s.find('am'))
print(s.rfind('am')) # 가장 앞 단어, 뒤로 찾기
print(s.count('am'))
print(s.capitalize())
print(s.title())
print(s.upper(), s.lower())
print(s.replace('steve', 'john'))

a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = "john"
family = "lee"
print(f'My name is {name} {family}. I am {family} {name}')