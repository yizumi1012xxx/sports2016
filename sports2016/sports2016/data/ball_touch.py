# -*- coding: utf-8 -*-
"""
This file include class related treating ball touch data.
"""

import common.file
import common.config
import common.path
from data.ball_touch_action import BallTouchAction

class BallTouchCustom():
    """
    This class treat ball touch data.
    """

    def __init__(self, match_id, match_status_id):
        self.__match_id = match_id
        self.__match_status_id = match_status_id
        self.__filepath = self.__get_filepath()
        self.__data = []
        self.__load()

    def __get_filepath(self):
        config = common.config.load()
        filepath = config["SPORTS_DATA_FOLDER_PATH"] + config["BALL_TOUCH_DATA_PATH"]
        return common.path.get_abs_pass(filepath)

    def __load(self):
        header, datas = common.file.read_csv(self.__filepath)
        for data in datas:
            data_match_id = int(data[header.index("matchID")])
            data_match_status_id = int(data[header.index("matchState")])
            if self.__match_id == data_match_id and self.__match_status_id == data_match_status_id:
                self.__data.append(BallTouchAction(header, data))

    def get_frames(self) -> [BallTouchAction]:
        """
        get_frames
        """
        return self.__data
