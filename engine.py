from __future__ import annotations
import time
from typing import TYPE_CHECKING

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap

class Engine:
    game_map: GameMap
    def __init__(self, player: Entity):
        self.event_handler: EventHandler = EventHandler(self)
        self.player = player

    def update_fov(self) -> None:
        """Recompute visible area based on player POV"""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        #if a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def handle_turns(self, action) -> None:
        print("##New round!##")
        entities_list = list(self.game_map.entities)
        entities_sorted = sorted(entities_list, key=lambda entity: entity.fighter.action_points, reverse=True)
        #sort enemies by remaining AP
        for entity in entities_sorted:
            entity.fighter.action_points += entity.fighter.speed * 10
        for entity in entities_sorted:

            if entity.ai:
                #player also has attribute AI.
                
                #TODO: move action cost to individual actions in actions.py
                while(entity.fighter.action_points >= 1000):    
                    if entity == self.player:
                        action.perform()
                        entity.fighter.action_points -= 1000
                    elif entity != self.player:
                        entity.ai.perform()
                        entity.fighter.action_points -= 1000
                    print(f'The {entity.name} takes its turn. AP: {entity.fighter.action_points}')
                    #time.sleep(.01)
                    self.update_fov() #Update FOV after each entity's turn

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        context.present(console)

        console.clear()