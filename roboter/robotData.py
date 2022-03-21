class Guest(object):

    name = []
    count = []

    def __init__(self):
        self._name = self.name
        self._count = self.count

    def Name(self):
        return self._name

    def Count(self, name):
        if self.isHadName(name):
            return self._count[self._name.index(name)]

        else:
            return 0

    def nameList(self):
        return self.name

    def countList(self):
        return self.count

    def Group(self):
        return [(a, b) for a, b in zip(self._name, self._count)]

    def defaultGroup(self, name, count):
        self._name = name
        self._count = count

    def appendGroup(self, name, count):
        self._name.append(name)
        self._count.append(count)

    def isHadName(self, name):
        is_had = True

        try:
            self.name.index(name)

        except:
            is_had = False

        return is_had
