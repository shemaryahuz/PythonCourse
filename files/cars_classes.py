
class Car:

    def __init__(self):

        self.speed = 0
        self.year = 0

class Cars(Car):

    def __init__(self):
        super().__init__()
        pass