s = """\
AAA
BBB    
CCC    
DDD
"""
with open("test.txt", 'r+') as f: # w+로 쓰기 읽기 가능 r+ 읽고 쓰기 가능
    print(f.read())
    # r+로 읽고 쓸 땐 이미 있는 파일만 가능
    f.seek(0)
    f.write(s)
    # print(f.read()) # !!! 주의 !!! w+는 읽고 쓰기 때문에, 이 읽기를 맨 앞에 두지 말 것

    # 'w' : 작성 및 파일 생성 'a' : append 파일에 내용 추가 'r' : 파일 읽어오기
    #f.write(s)
    #print('My', 'name', 'is', 'Mike', sep='#', end='!', file = f)
    # f.close() 메모리를 계속 사용하기 때문에 닫아야함.

#with open('test.txt', 'r') as f:
    #print(f.read()) # 파일을 전부 읽어옴.
    #while True:
    #    chunk = 2 # 라인당 문자 단위로 2면 2글자씩
    #    line = f.readline(chunk) # 줄단위
    #    print(line) # end=''는 줄바꿈 방지
    #    if not line:
    #       break
    #print(f.tell())
    #print(f.read(1))
    #f.seek(5)
    #print(f.read(1))
    #f.seek(14)
    #print(f.read(1))
    #f.seek(15)
    #print(f.read(1))
    #f.seek(5)
    #print(f.read(1))