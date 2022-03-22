class Group(object):
    name = []
    count = []

    def __init__(self):
        self._name = self.name
        self._count = self.count

    def countPlus(self, name):
        self._count[self._name.index(name)] = str(int(self._count[self._name.index(name)]) + 1)

    def Group(self):
        return [(name, count) for name, count in zip(self._name, self._count)]

    def defaultGroup(self, name, count):
        self._name = name
        self._count = count


class People(Group):
    name = []
    count = []

    def __init__(self):
        super().__init__()

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


class Rest(Group):
    name = []
    count = []
    
    def __init__(self):
        super().__init__()

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

    def isRestExist(self):
        try:
            if self._name[0]:
                return True
        except:
            return False
