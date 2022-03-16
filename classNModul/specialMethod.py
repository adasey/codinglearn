class Word(object):

    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return "word!!!!"

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w = Word("Hello")
w2 = Word(" and How are you")
print(w) # __str__ 함수 호출
print(len(w)) # len(w.text) 해당 속성의 text 길이를 재야하나, 개체의 특수 메소드를 사용해 바로 길이 계산 가능
print(w + w2) # 마치 c나 c++의 연산자처럼 __add__ 호출. 객체의 더하기로도 가능 str이 아닌 단순 연산도 가능
print(w == w2) # __eq__를 통해 호출되며, __eq__를 제거 시 개체끼리의 비교이므로 같지 않음.

print(id(w))
print(id(w2))

""" 많이 사용 시 *
__eq__(self, other) self == other
__ne__(self, other) self != other
__lt__(self, other) self < other
__gt__(self, other) self > other
__le__(self, other) self <= other
__ge__(self, other) self >= other

__add__(self, other) self + other
__sub__(self, other) self - other
__mul__(self, other) self * other
__floordiv__(self, other) self // other
__truediv__(self, other) self / other
__mod__(self, other) self % other
__pow__(self, other) self ** other

__str__(self) str(self) *
__len__(self) len(self)
"""