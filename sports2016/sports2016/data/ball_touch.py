# -*- coding: utf-8 -*-
"""
This file include class related treating ball touch data.
"""

import common.path as path
import common.file as file
import common.flag as flag

class BallTouchCustom():
    """
    This class treat ball touch data.
    """

    def __init__(self, filepath):
        self.__filepath = filepath
        self.__data = []
        self.__load()

    def __load(self):
        header, datas = file.read_csv(self.__filepath)
        for data in datas:
            self.__data.append(BallTouchAction(header, data))

    def get_match_actions(self, match_id, match_status_id):
        """
        get match actions by match_id and match_status_id
        """
        ret = []
        for data in self.__data:
            __match_id = data[self.__header.index("matchID")]
            __match_states_id = data[self.__header.index("matchState")]
            if(__match_id == match_id and __match_states_id == match_status_id):
                pass

class BallTouchAction():
    """
    This class treat ball touch action data.
    """

    def __init__(self, header, data):
        self.match_id = data[header.index("matchID")]
        self.match_status_id = data[header.index("matchState")]
        self.frame_id = data[header.index("frameID")]
        self.team_id = data[header.index("teamID")]
        # タッチプレイヤーID: 背番号に変換する必要あり.
        self.player_id = data[header.index("playerID")]
        # ballタッチプレイヤーがhome or away
        self.homeaway = data[header.index("homeaway")]
        self.ball_x = data[header.index("ballX")]
        self.ball_y = data[header.index("ballY")]
        # self.attack_no = data[header.index("attackNo")]
        # self.history_id = data[header.index("historyID")]

    def get_match_id(self):
        """
        Get match_id.
        """
        return self.match_id

    def get_match_status_id(self):
        """
        Get match_status_id.
        """
        return self.match_status_id

    def get_frame_id(self):
        """
        Get frame_id.
        """
        return self.frame_id

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

    def get_homeaway(self):
        """
        Get home-away constant.
        home:1, away:2
        """
        return self.homeaway

    def get_ball_x(self):
        """
        Get x-coordinate of ball.
        """
        return self.ball_x

    def get_ball_y(self):
        """
        Get y-coordinate of ball.
        """
        return self.ball_y
