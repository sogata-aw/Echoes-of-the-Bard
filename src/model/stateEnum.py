from enum import Enum

class StateEnum(Enum):
    playing = "playing"
    in_menu = "in_menu"
    in_credit = "in_credit"
    finished = "finished"