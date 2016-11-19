# -*- coding: utf-8 -*-
"""
ball_touch_action.py
"""

class BallTouchAction():
    """
    BallTouchAction
    """

    HOME = 1
    AWAY = 2

    def __init__(self, frame_id: int, history_id: int, team_id: int,
                 player_id: int, homeaway: int, ball_x: float, ball_y: float):
        self.frame_id = frame_id
        self.history_id = history_id
        self.team_id = team_id
        self.player_id = player_id
        self.homeaway = homeaway
        self.ball_x = ball_x
        self.ball_y = ball_y

    def get_frame_id(self) -> int:
        """
        get_frame_id
        """
        return self.frame_id

    def get_history_id(self) -> int:
        """
        get_history_id
        """
        return self.history_id

    def get_team_id(self) -> int:
        """
        get_team_id
        """
        return self.team_id

    def get_player_id(self) -> int:
        """
        get_player_id
        """
        return self.player_id

    def is_home(self) ->bool:
        """
        is_home
        """
        if self.homeaway == self.AWAY:
            return False
        elif self.homeaway == self.HOME:
            return True
        else:
            raise ValueError("homeawayが不正です。")

    def get_ball_x(self) -> float:
        """
        get_ball_x
        """
        return self.ball_x / 3.

    def get_ball_y(self) -> float:
        """
        get_ball_y
        """
        return self.ball_y / 3. * -1.
