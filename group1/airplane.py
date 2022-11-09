from utils import get_random_int, get_random_string


class Airplane:
    def __init__(self):
        self.name = get_random_string()
        self.speed = get_random_int()
        self.height_above_sea_level = get_random_int(2000, 10000)
        self.number_of_passengers = get_random_int(50, 200)

    def notify(self, message):
        print('Airplane ({}) got message {}'.format(self.name, message))
