count = 0

while count < 0: # while 내부 break가 없을 때 해당 조건문을 달성하면
    if count == 2: 
        break #이게 있다면 else로 가지 않음
    print(count)
    count += 1

#else: # 이 문장을 실행하고 종료
#    print("finish job")

#while Input 문 입력문
while False:
    key_word = input('Enter: ')
    if key_word == 'ok':
        break
    print('not correct')

# for else 마찬가지로 break가 있다면 else문 실행은 없음

for fruit in ['apple', 'banana', 'orange', 'grape']:
    if fruit == 'banana':
        print("orange and grape are sold out")
        break
    
    print(fruit)

else:
    print("all fruit sold!")

# for dictionary
d = {'x':100, 'y':200}

print(d.items()) # 해당 dictionary를 items로 호출하면 tuple내로 들어간 채로 호출

for k, v in d.items():
    print(k, ':', v)