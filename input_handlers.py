from typing import Optional

import tcod.event
from actions import Action, BumpAction, EscapeAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.KeySym.KP_1:
            action = BumpAction(dx=-1, dy=1)
        if key == tcod.event.KeySym.KP_2:
            action = BumpAction(dx=0, dy=1)
        if key == tcod.event.KeySym.KP_3:
            action = BumpAction(dx=1, dy=1)
        if key == tcod.event.KeySym.KP_4:
            action = BumpAction(dx=-1, dy=0)
        if key == tcod.event.KeySym.KP_5:
            action = BumpAction(dx=0, dy=0)
        if key == tcod.event.KeySym.KP_6:
            action = BumpAction(dx=1, dy=0)
        if key == tcod.event.KeySym.KP_7:
            action = BumpAction(dx=-1, dy=-1)
        if key == tcod.event.KeySym.KP_8:
            action = BumpAction(dx=0, dy=-1)
        if key == tcod.event.KeySym.KP_9:
            action = BumpAction(dx=1, dy=-1)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action