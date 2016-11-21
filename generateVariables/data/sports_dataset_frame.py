# -*- coding: utf-8 -*-
"""
sports_dataset_frame.py
"""

from data.sports_dataset_frame_player import SportsDatasetFramePlayer

class SportsDatasetFrame():
    """
    SportsDatasetFrame
    """

    def __init__(self, match_status_id: int, frame_id: int, history_id: int,
                 ball_x: float, ball_y: float,
                 ball_player: SportsDatasetFramePlayer,
                 home_players: [SportsDatasetFramePlayer],
                 away_players: [SportsDatasetFramePlayer],
                 home_attack_direction: bool,
                 away_attack_direction: bool):
        self.__match_status_id = match_status_id
        self.__frame_id = frame_id
        self.__history_id = history_id
        self.__ball_x = ball_x
        self.__ball_y = ball_y
        self.__ball_player = ball_player
        self.__home_players = home_players
        self.__away_players = away_players
        self.__home_attack_direction = home_attack_direction
        self.__away_attack_direction = away_attack_direction

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

    def get_home_attack_direction(self) -> bool:
        """
        get_home_attack_direction
        True: positive, False: negative
        """
        return self.__home_attack_direction

    def get_away_attack_direction(self) -> bool:
        """
        get_away_attack_direction
        True: positive, False: negative
        """
        return self.__away_attack_direction

    def get_home_players_points(self):
        """
        get_home_players_points
        """
        return self.__get_players_points(self.get_home_players())

    def get_away_players_points(self):
        """
        get_away_players_points
        """
        return self.__get_players_points(self.get_away_players())

    @staticmethod
    def __get_players_points(players: [SportsDatasetFramePlayer]):
        players_x = []
        players_y = []
        for player in players:
            players_x.append(player.get_x())
            players_y.append(player.get_y())
        return players_x, players_y
