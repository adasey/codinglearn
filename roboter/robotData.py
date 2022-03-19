class People():

    name = []
    restaurant = []

    def __init__(self):
        self._name = self.name
        self._restaurant = self.restaurant

    @property
    def getName(self):
        return self._name

    @name.setter
    def setName(self, name):
        self._name = name

    @property
    def getRest(self):
        return self._restaurant

    @name.setter
    def setRest(self, restaurant):
        self._restaurant = restaurant

    def appendName(self, name):
        self._name.append(name)

    def appendRest(self, restaurant):
        self._restaurant.append(restaurant)