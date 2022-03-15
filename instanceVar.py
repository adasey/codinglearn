class Person(object):
    
    kind = "human"

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

class Truck(object):
    
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

c = Truck()
c.add_word("add 1")
c.add_word("add 2")
print(c.words)

d = Truck()
d.add_word("add 3")
d.add_word("add 4")
print(d.words)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()