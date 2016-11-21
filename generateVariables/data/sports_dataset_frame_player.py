# -*- coding: utf-8 -*-
"""
sports_dataset_frame_player.py
"""

class SportsDatasetFramePlayer():
    """
    SportsDatasetFramePlayer
    """

    def __init__(self, player_id: int, player_is_home: bool, player_x: float, player_y: float):
        self.__id = player_id
        self.__is_home = player_is_home
        self.__x = player_x
        self.__y = player_y

    def get_id(self) -> int:
        """
        get_id
        """
        return self.__id

    def is_home(self) -> bool:
        """
        is_home
        """
        return self.__is_home

    def get_x(self) -> float:
        """
        get_x
        """
        return self.__x

    def get_y(self) -> float:
        """
        v
        """
        return self.__y
