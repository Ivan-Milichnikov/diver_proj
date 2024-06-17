from aiogram.fsm.state import StateGroup,State

class StartQuestion(StateGroup):
    q1 = State()
    q2 = State()