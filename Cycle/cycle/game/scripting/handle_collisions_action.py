import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # snake = cast.get_first_actor("snakes")
        # head = snake.get_segments()[0]
        # segments = snake.get_segments()[1:]

        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")

        cycle_one_head = cycle_one.get_cycle()
        cycle_two_head = cycle_two.get_cycle()
        
        segments_one = cycle_one.get_segments()[1:]
        segments_two = cycle_two.get_segments()[1:]
        
        # for segment_one in segments_one:
        #     if cycle_two_head.get_position().equals(segment.get_position()):
                #reduce points
                #code to game over if point < 1
        
        # for segment_two in segments_two:
        #     if cycle_one_head.get_position().equals(segment.get_position()):
                #reduce points
                #code to game over if point < 1
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)