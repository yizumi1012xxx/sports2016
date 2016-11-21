# -*- coding: utf-8 -*-
"""
ball_touch.py
"""

from common.common import Config, File, Path
from data.ball_touch_action import BallTouchAction

class BallTouchCustom():
    """
    BallTouchCustom
    """

    def __init__(self, match_id, match_status_id):
        self.__match_id = match_id
        self.__match_status_id = match_status_id
        self.__filepath = self.__get_filepath()
        self.__columns = []
        self.__rows = []
        self.__frames = []
        self.__load()
        self.__get_frames()

    def __get_filepath(self) -> str:
        config = Config.load()
        filepath = config["SPORTS_DATA_FOLDER_PATH"] + config["BALL_TOUCH_DATA_PATH"]
        return Path.get_abs_pass(filepath)

    def __load(self) -> None:
        self.__columns, self.__rows = File.read_csv(self.__filepath)

    def __get_frames(self) -> None:
        for data in self.__rows:
            match_id = int(data[self.__columns.index("matchID")])
            match_status_id = int(data[self.__columns.index("matchState")])
            if self.__match_id == match_id and self.__match_status_id == match_status_id:
                frame_id = int(data[self.__columns.index("frameID")])
                history_id = data[self.__columns.index("historyID")]
                team_id = int(data[self.__columns.index("teamID")])
                player_id = int(data[self.__columns.index("playerID")])
                homeaway = int(data[self.__columns.index("homeaway")])
                ball_x = float(data[self.__columns.index("ballX")])
                ball_y = float(data[self.__columns.index("ballY")])
                self.__frames.append(BallTouchAction(
                    frame_id, history_id, team_id, player_id, homeaway, ball_x, ball_y))

    def get_frames(self) -> [BallTouchAction]:
        """
        get_frames
        """
        return self.__frames
