from enum import Enum

class StateEnum(Enum):
    paused = "paused"
    playing = "playing"
    in_menu = "in_menu"
    in_credit = "in_credit"
    finished = "finished"