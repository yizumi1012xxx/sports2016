# -*- coding: utf-8 -*-
"""
This file marge ball_touch data and tracking data.
"""

class SportsDatasetFramePlayer():
    """
    SportsDatasetFramePlayer
    """

    def __init__(self, player_id, player_is_home, player_x, player_y):
        self.__id = player_id
        self.__is_home = player_is_home
        self.__x = player_x
        self.__y = player_y

    def get_id(self):
        """
        get_id
        """
        return self.__id

    def is_home(self):
        """
        is_home
        """
        return self.__is_home

    def get_x(self):
        """
        get_x
        """
        return self.__x

    def get_y(self):
        """
        v
        """
        return self.__y
