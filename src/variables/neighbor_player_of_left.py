# -*- coding: utf-8 -*-
"""
neighbor_player_of_left.py
"""

from data.sports_dataset_frame import SportsDatasetFrame

class NeighborPlayerOfLeft:
    """
    NeighborPlayerOfLeft
    トラッキングデータの座標に基づき，ボール保持プレイヤーの左方の状況を出力する。
    """
    NONE_EXIST = 0
    HOME_EXIST = 1
    AWAY_EXIST = 2
    BOTH_EXIST = 3

    THRESHOLD_DISTANCE = 5.


    def __init__(self):
        self.__sports_dataset_frame = None
        self.__match_status_id = None
        self.__ball_player = None
        self.__home_players = []
        self.__home_players_x = []
        self.__home_players_y = []
        self.__away_players = []
        self.__away_players_x = []
        self.__away_players_y = []

    def __set_frame(self, frame: SportsDatasetFrame):
        self.__sports_dataset_frame = frame
        self.__match_status_id = self.__sports_dataset_frame.get_match_status_id()
        self.__ball_player = self.__sports_dataset_frame.get_ball_player()

        self.__home_players = self.__sports_dataset_frame.get_home_players()
        self.__home_players_x, self.__home_players_y =\
            self.__sports_dataset_frame.get_home_players_points()

        self.__away_players = self.__sports_dataset_frame.get_away_players()
        self.__away_players_x, self.__away_players_y =\
            self.__sports_dataset_frame.get_away_players_points()

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
        return self.__get_value()

    def __get_value(self):
        """
        __get_value
        """
        if self.__ball_player is None:
            return self.NONE_EXIST

        # 0. フラグを準備
        away_flg = False
        home_flg = False

        # 1. ボールを持っているプレイヤーのチームをチェック
        # ball_player_is_home = self.__ball_player.is_home()
        ball_player_x = self.__ball_player.get_x()
        ball_player_y = self.__ball_player.get_y()

        # 2. 角度と距離によってフラグを更新
        for player in self.__home_players:
            player_x = player.get_x()
            player_y = player.get_y()
            distance = self.__calculate_distance(ball_player_x, ball_player_y, player_x, player_y)
            if distance < self.THRESHOLD_DISTANCE:
                if self.__calculate_direction(ball_player_x, ball_player_y, player_x, player_y):
                    home_flg = True

        for player in self.__away_players:
            player_x = player.get_x()
            player_y = player.get_y()
            distance = self.__calculate_distance(ball_player_x, ball_player_y, player_x, player_y)
            if distance < self.THRESHOLD_DISTANCE:
                if self.__calculate_direction(ball_player_x, ball_player_y, player_x, player_y):
                    away_flg = True

        if away_flg and home_flg:
            return self.BOTH_EXIST
        elif away_flg and not home_flg:
            return self.AWAY_EXIST
        elif not away_flg and home_flg:
            return self.HOME_EXIST
        elif not away_flg and not home_flg:
            return self.NONE_EXIST

    @staticmethod
    def __calculate_distance(x_1, y_1, x_2, y_2):
        return ((x_1-x_2)**2. + (y_1-y_2)**2.)**.5

    @staticmethod
    def __calculate_direction(x_1, y_1, x_2, y_2):
        return (y_2 - y_1) >= 0 and abs(x_2 - x_1) <= abs(y_2 - y_1)
