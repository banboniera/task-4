from typing import Union

from airplane import Airplane
from fighter import Fighter
from helicopter import Helicopter


class TrafficController:
    def __init__(self):
        self.airplane_list = []
        self.fighter_list = []
        self.helicopter_list = []

    def add(self, instance: Union['Airplane', 'Fighter', 'Helicopter']):
        class_name = instance.__class__
        if class_name == Airplane:
            return self.airplane_list.append(instance)
        elif class_name == Fighter:
            return self.fighter_list.append(instance)
        elif class_name == Helicopter:
            return self.helicopter_list.append(instance)

    def notify_all(self, message="Bad weather be careful"):
        for instance in self.airplane_list:
            instance.notify(message)

        for instance in self.fighter_list:
            instance.notify(message)

        for instance in self.airplane_list:
            instance.notify(message)
