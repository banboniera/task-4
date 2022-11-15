from airplane import Airplane
from fighter import Fighter
from helicopter import Helicopter
from traffic_controller import TrafficController
from utils import get_random_int


def main():
    tf = TrafficController()

    for i in range(get_random_int(1, 3)):
        tf.add(Airplane())

    for i in range(get_random_int(1, 3)):
        tf.add(Fighter())

    for i in range(get_random_int(1, 3)):
        tf.add(Helicopter())

    tf.notify_all()


if __name__ == "__main__":
    main()
