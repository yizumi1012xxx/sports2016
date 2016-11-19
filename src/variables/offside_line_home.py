# -*- coding: utf-8 -*-
"""
offside_line_home.py
"""

from common.common import Util
from data.sports_dataset_frame import SportsDatasetFrame

class OffsideLineHome:
    """
    OffsideLineHome
    """

    FIRST_TIME = 1
    SECOND_TIME = 2

    def __init__(self):
        self.__sports_dataset_frame = None
        self.__match_status_id = None
        self.__home_players = []
        self.__home_players_x = []
        self.__home_players_y = []
        self.__away_players = []
        self.__away_players_x = []
        self.__away_players_y = []

    def __set_frame(self, frame: SportsDatasetFrame):
        self.__sports_dataset_frame = frame
        self.__match_status_id = self.__sports_dataset_frame.get_match_status_id()

        self.__home_players = self.__sports_dataset_frame.get_home_players()
        self.__home_players_x, self.__home_players_y =\
            self.__sports_dataset_frame.get_home_players_points()

        # self.__away_players = self.__sports_dataset_frame.get_away_players()
        # self.__away_players_x, self.__away_players_y =\
        #     self.__sports_dataset_frame.get_away_players_points()

    def get_name(self):
        """
        get_name
        """
        return self.__class__.__name__

    def get_value(self, frame: SportsDatasetFrame):
        """
        get_value
        """
        self.__set_frame(frame)
        return self.__get_offside_line()

    def __get_offside_line(self):
        """
        自チームで2番目に後方のx座標を取得
        """
        if self.__match_status_id == self.FIRST_TIME:
            return Util.min2(self.__home_players_x)
        elif self.__match_status_id == self.SECOND_TIME:
            return Util.max2(self.__home_players_x)
