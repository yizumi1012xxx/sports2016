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
        config = common.config.load()
        self.__filepath = common.path.get_abs_pass(
            config["SPORTS_DATA_FOLDER_PATH"] + config["BALL_TOUCH_DATA_PATH"])
        self.__match_id = match_id
        self.__match_status_id = match_status_id
        self.__data = []
        # load
        header, datas = common.file.read_csv(self.__filepath)
        for data in datas:
            data_match_id = data[header.index("matchID")]
            data_match_status_id = data[header.index("matchState")]
            if self.__match_id == data_match_id and self.__match_status_id == data_match_status_id:
                self.__data.append(BallTouchAction(header, data))

    def get_frames(self) -> [BallTouchAction]:
        """
        get_frames
        """
        return self.__data
