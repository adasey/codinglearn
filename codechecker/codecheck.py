x = 1  # O
y = 2; # X

x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' # 80개 이내로 하기

def test_func(x, y, z, sdafsdaassfdassdasfasdfassafdasfasfsdfasdfasf='test'): #

    """
    sadlkfjlaksdjflkjsaldkfjlksdjflksdlkfjlskdjflksjlkdfjlksjflkdjklsdjlkfjksfsdfkjlskdf 설명 url 삽입 시 80개가 넘어도 ㄱㅊ
    """
    print(x)

if x and y: # 필요없이 괄호 X
    print("exist") # tab 공간은 스페이스 4번 추천 2개 혹은 4개 난 4개

    x = { # 딕셔너리도 tab
        "test" : "sss",
        "get" : "x"
    }

    y = {"exits" : "a"} # 스페이스 없이
    
    x, y = 3, 4

    x = y + x

    x = 10
    yyyyyyy = 100
    zzzzzzzzz = 10001

word = "hello"
word2 = "!"

new_word = f'{word}!!!{word2}' # 변수 중간에 문자열이 삽입될 시 이 연결이 더 좋다.

new_word = word + word2 # 위의 연결보단 이 연결이 더 좋음.

long_word = []
for word in ["sdafas", "asdfsadfdsa", "asdfasdf"]:
    # long_word += f'{word}asdf as' 이거보단
    long_word.append(f'{word}asdf as')

new_long_word = ''.join(long_word) # 결국 이게 제일 좋음. 메모리 측면 이득

print("", '') # "", '' 의 차이는 규칙에 맞춰서 "'"안에 '가 들어가는 경우 ""가 더 좋음.

if x: print("exist")
else: print("no")