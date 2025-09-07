from enum import Enum


class StateEnum(Enum):
    playing = "playing"
    in_menu = "in_menu"
    levels="levels"
    explanation="explanation"
    in_credit = "in_credit"
    finished = "finished"

