from utils import get_random_int, get_random_string


class Helicopter:
    def __init__(self):
        self.name = get_random_string()
        self.speed = get_random_int(200, 400)
        self.height_above_sea_level = get_random_int(1000, 4000)
        self.owner = get_random_string(6)

    def notify(self, message):
        print('Helicopter ({}) with owner {} got message {}'.format(
            self.name, self.owner, message))
