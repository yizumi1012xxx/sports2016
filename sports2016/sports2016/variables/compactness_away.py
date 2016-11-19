# -*- coding: utf-8 -*-
"""
This file get compactness of away team from one frame data.
"""

from data.sports_dataset_frame import SportsDatasetFrame
import common.util

class CompactnessAway:
    """
    CompactnessAway
    """

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

        # self.__home_players = self.__sports_dataset_frame.get_home_players()
        # self.__home_players_x = []
        # self.__home_players_y = []
        # for player in self.__home_players:
        #     self.__home_players_x.append(player.get_x())
        #     self.__home_players_y.append(player.get_y())

        self.__away_players = self.__sports_dataset_frame.get_away_players()
        self.__away_players_x = []
        self.__away_players_y = []
        for player in self.__away_players:
            self.__away_players_x.append(player.get_x())
            self.__away_players_y.append(player.get_y())

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
        return abs(self.__get_attack_line() - self.__get_offside_line())

    def __get_attack_line(self):
        """
        自チームで1番先頭のx座標を取得
        前半：最大値, 後半：最小値
        """
        if self.__match_status_id == 1:
            return min(self.__away_players_x)
        elif self.__match_status_id == 2:
            return max(self.__away_players_x)

    def __get_offside_line(self):
        """
        自チームで2番目に後方のx座標を取得
        """
        if self.__match_status_id == 1:
            return common.util.max2(self.__away_players_x)
        elif self.__match_status_id == 2:
            return common.util.min2(self.__away_players_x)
