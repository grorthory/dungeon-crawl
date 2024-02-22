from __future__ import annotations

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
        for entity in self.game_map.entities:
            if entity.ai:
                #player also has attribute AI.
                if entity == self.player:
                    action.perform()
                elif entity != self.player:
                    entity.ai.perform()
                entity.fighter.action_points = entity.fighter.speed * 10
                print(f'The {entity.name} takes its turn. AP: {entity.fighter.action_points}')
                self.update_fov() #Update FOV after each entity's turn

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        context.present(console)

        console.clear()