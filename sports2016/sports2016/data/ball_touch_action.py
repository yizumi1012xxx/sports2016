# -*- coding: utf-8 -*-
"""
This file include class related treating ball touch data.
"""

class BallTouchAction():
    """
    This class treat ball touch action data.
    """

    HOME = 1
    AWAY = 2

    def __init__(self, header, data):
        self.frame_id = int(data[header.index("frameID")])
        self.history_id = data[header.index("historyID")]
        self.team_id = int(data[header.index("teamID")])
        self.player_id = int(data[header.index("playerID")])
        self.homeaway = int(data[header.index("homeaway")])
        self.ball_x = float(data[header.index("ballX")])
        self.ball_y = float(data[header.index("ballY")])
        # self.attack_no = data[header.index("attackNo")]

    def get_frame_id(self):
        """
        Get frame_id.
        """
        return self.frame_id

    def get_history_id(self):
        """
        Get histroy_id.
        """
        return self.history_id

    def get_team_id(self):
        """
        Get team_id.
        """
        return self.team_id

    def get_player_id(self):
        """
        Get player_id.
        """
        return self.player_id

    def is_home(self):
        """
        Get home-away constant.
        home:1, away:2
        """
        if self.homeaway == 2:
            return False
        elif self.homeaway == 1:
            return True
        else:
            raise ValueError("homeawayが不正です。")

    def get_ball_x(self):
        """
        Get x-coordinate of ball.
        """
        return self.ball_x / 3.

    def get_ball_y(self):
        """
        Get y-coordinate of ball.
        """
        return self.ball_y / 3. * -1.
