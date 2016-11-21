# -*- coding: utf-8 -*-
"""
tracking_frame_player.py
"""

class TrackingFramePlayer():
    """
    TrackingFramePlayer
    """
    AWAY = 0
    HOME = 1

    def __init__(self, frame_id: int, team_id: int, system_target_id: int, uniform_number: int,
                 point_x: float, point_y: float, velocity: float):
        self.__frame_id = frame_id
        self.__team_id = team_id
        self.__system_target_id = system_target_id
        self.__uniform_number = uniform_number
        self.__point_x = point_x
        self.__point_y = point_y
        self.__velocity = velocity

    def get_frame_id(self) -> int:
        """
        get_frame_id
        """
        return self.__frame_id

    def is_home(self) -> bool:
        """
        get_team_id
        away:0, home:1, 審判:3, 不明:4
        """
        if self.__team_id == 0:
            return False
        elif self.__team_id == 1:
            return True
        else:
            raise ValueError("team_idが不正です。[%s]"%self.__team_id)

    def get_uniform_number(self) -> int:
        """
        get_uniform_number
        """
        return self.__uniform_number

    def get_point_x(self) -> float:
        """
        get_point_x
        """
        return self.__point_x / 100.

    def get_point_y(self) -> float:
        """
        get_point_y
        """
        return self.__point_y / 100.
