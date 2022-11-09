from utils import get_random_int, get_random_string


class Fighter:
    def __init__(self):
        self.name = get_random_string()
        self.speed = get_random_int()
        self.height_above_sea_level = get_random_int(1000, 12000)
        self.pilot = get_random_string(4)

    def notify(self, message):
        print('Fighter ({}) with pilot {} got message {}'.format(
            self.name, self.pilot, message))
