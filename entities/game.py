from time import sleep
from typing import List

from entities.map import Map


class Game:
    def __init__(self, glider: List[list], sleep_timer=0.1):
        self.map = Map(glider)
        self.sleep_timer = sleep_timer

    def start(self):
        self.map.print()
        while True:
            sleep(self.sleep_timer)
            self.map.next_generation()
            self.map.print()



