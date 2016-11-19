# -*- coding: utf-8 -*-
"""
sports_dataset_frame.py
"""

from data.sports_dataset_frame_player import SportsDatasetFramePlayer

class SportsDatasetFrame():
    """
    SportsDatasetFrame
    """

    def __init__(self, match_status_id, frame_id, history_id, ball_x, ball_y, ball_player, home_players, away_players):
        self.__match_status_id = match_status_id
        self.__frame_id = frame_id
        self.__history_id = history_id
        self.__ball_x = ball_x
        self.__ball_y = ball_y
        self.__ball_player = ball_player
        self.__home_players = home_players
        self.__away_players = away_players

    def get_match_status_id(self) -> int:
        """
        get_match_status_id
        """
        return self.__match_status_id

    def get_frame_id(self) -> int:
        """
        get_frame_id
        """
        return self.__frame_id

    def get_history_id(self) -> int:
        """
        get_history_id
        """
        return self.__history_id

    def get_ball_x(self) -> float:
        """
        get_ball_x
        """
        return self.__ball_x

    def get_ball_y(self) -> float:
        """
        get_ball_y
        """
        return self.__ball_y

    def get_ball_player(self) -> SportsDatasetFramePlayer:
        """
        get_ball_player
        """
        return self.__ball_player

    def get_home_players(self) -> [SportsDatasetFramePlayer]:
        """
        get_home_players
        """
        return self.__home_players

    def get_away_players(self) -> [SportsDatasetFramePlayer]:
        """
        get_away_players
        """
        return self.__away_players
