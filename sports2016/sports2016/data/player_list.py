# -*- coding: utf-8 -*-
"""
This file include class related treating player list.
"""

import common.config
import common.path
import common.file

class PlayerList():
    """
    This class treat player list.
    """

    def __init__(self):
        self.__filepath = self.__get_file_path()
        self.__columns = []
        self.__rows = []
        self.__load()

    def __get_file_path(self):
        config = common.config.load()
        path = \
            config["SPORTS_DATA_FOLDER_PATH"] +\
            config["BALL_TOUCH_DATA_FOLDER_PATH"] +\
            config["BALL_TOUCH_PLAYER_LIST_PATH"]
        return common.path.get_abs_pass(path)

    def __load(self):
        self.__columns, self.__rows = common.file.read_csv(self.__filepath)

    def get_player_id(self, match_id, is_home, uniform_number):
        """
        get_player_id
        """
        if is_home:
            homeaway_f = 1
        else:
            homeaway_f = 2

        for row in self.__rows:
            _homeaway_f = int(row[self.__columns.index("ホームアウェイF")])
            _match_id = int(row[self.__columns.index("試合ID")])
            _uniform_number = int(row[self.__columns.index("背番号")])
            _player_id = int(row[self.__columns.index("選手ID")])

            if _homeaway_f == homeaway_f\
                and _match_id == match_id\
                and _uniform_number == uniform_number:
                return _player_id
        raise ValueError("プレイヤーが存在しませんでした。")
