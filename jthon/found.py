
class Found:
    def __init__(self, key, value, siblings, parent=None):
        self.key = key
        self.value = value
        self.siblings = siblings
        #self.parent = parent

    def __str__(self):
        return '<Found {}>'.format({self.key: self.value})

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

    def __eq__(self, value):
        return {self.key: self.value}
