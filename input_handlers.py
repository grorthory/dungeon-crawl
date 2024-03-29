from __future__ import annotations
from typing import Optional, TYPE_CHECKING

import tcod.event
from actions import Action, BumpAction, EscapeAction
if TYPE_CHECKING:
    from engine import Engine


class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            self.engine.handle_turns(action)
    
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        if key == tcod.event.KeySym.KP_1:
            action = BumpAction(player, dx=-1, dy=1)
        if key == tcod.event.KeySym.KP_2:
            action = BumpAction(player, dx=0, dy=1)
        if key == tcod.event.KeySym.KP_3:
            action = BumpAction(player, dx=1, dy=1)
        if key == tcod.event.KeySym.KP_4:
            action = BumpAction(player, dx=-1, dy=0)
        if key == tcod.event.KeySym.KP_5:
            action = BumpAction(player, dx=0, dy=0)
        if key == tcod.event.KeySym.KP_6:
            action = BumpAction(player, dx=1, dy=0)
        if key == tcod.event.KeySym.KP_7:
            action = BumpAction(player, dx=-1, dy=-1)
        if key == tcod.event.KeySym.KP_8:
            action = BumpAction(player, dx=0, dy=-1)
        if key == tcod.event.KeySym.KP_9:
            action = BumpAction(player, dx=1, dy=-1)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction(player)

        # No valid key was pressed
        return action