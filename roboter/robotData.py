class Group(object):
    name = []
    count = []

    def __init__(self):
        self._name = self.name
        self._count = self.count

    def countPlus(self, name):
        self._count[self._name.index(name)] = str(int(self._count[self._name.index(name)]) + 1)

    def Group(self):
        return [ (name, count) for name, count in zip(self._name, self._count)]


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

    @property
    def Name(self):
        return self._name

    def Count(self, name):
        if self.isHadName(name):
            return self._count[self._name.index(name)]

        else:
            return 0

    @property
    def countList(self):
        return self._count

    def setGroupSorted(self):
        temp = self.groupDict()
        sorted = self.groupSort()

        self._name = sorted
        i = 0

        for key in sorted:
            self._count[i] = temp[key]

            i += 1

    def groupSort(self):
        return sorted(self.groupDict(), key=self.groupDict().__getitem__, reverse=True)

    def groupDict(self):
        return { name : count for name, count in zip(self._name, self._count)}

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

    def isHadSecond(self):
        is_second = True

        try:
            self.name[1]

        except:
            is_second = False

        return is_second

    def isRestExist(self):
        try:
            if self._name[0]:
                return True
        except:
            return False
