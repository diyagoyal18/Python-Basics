#public


class abc:
    def __init__(self):
        self.public=10

    def publicFunc():
        pass

obj1=abc()
obj1.publicFunc()


# #private
# use 2 __
class abc:
    def __init__(self):
        self.public=10

    def __privateFunc():
        pass

obj1=abc()
obj1.__privateFunc()


# #protected
# use 1 _

