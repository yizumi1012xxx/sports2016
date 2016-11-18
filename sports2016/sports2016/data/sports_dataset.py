# -*- coding: utf-8 -*-
"""
This file marge ball_touch data and tracking data.
"""

import common.util

from data.ball_touch import BallTouchCustom
from data.tracking import Tracking
from data.sports_dataset_frame import SportsDatasetFrame

class SportsDataset():
    """
    SportsDataset
    """

    def __init__(self, match_id, match_status_id):
        self.__match_id = int(match_id)
        self.__match_status_id = int(match_status_id)
        self.__ball_touch = BallTouchCustom(self.__match_id, self.__match_status_id)
        self.__tracking = Tracking(self.__match_id, self.__match_status_id)

        frames = self.__ball_touch.get_frames()
        for frame in frames:
            # ball_touch frame
            frame_id = frame.get_frame_id()
            ball_x = frame.get_ball_x()
            ball_y = frame.get_ball_y()
            attacker_is_home = frame.is_home()
            attacker_id = frame.get_player_id()
            attacker = None
            attack_team_player = []
            defense_team_player = []

            # tracking frame
            for player in self.__tracking.find_tracking_frame_players(frame_id):
                try:
                    player_x = player.get_point_x()
                    player_y = player.get_point_y()
                    player_is_home = player.is_home()
                    player_id = self.__get_player_id(player_is_home, player.get_uniform_number())
                    sports_dataset_frame_player = SportsDatasetFramePlayer(
                        player_id, player_x, player_y)

                    if player_is_home == attacker_is_home:
                        attack_team_player.append(sports_dataset_frame_player)
                    elif player_is_home != attacker_is_home:
                        defense_team_player.append(sports_dataset_frame_player)

                    if attacker_id == player_id:
                        attacker = sports_dataset_frame_player
                except ValueError:
                    pass
            sports_dataset_frame = SportsDatasetFrame(frame_id, ball_x, ball_y, attacker,
                                                      attack_team_player, defense_team_player)

    def get_frames(self):
        pass

    def __get_player_id(self, is_home, uniform_number):
        return common.util.convert_uniform_number_to_player_id(self.__match_id, is_home, uniform_number)

class SportsDatasetFramePlayer():

    def __init__(self, id, x, y):
        self.__id = id
        self.__x = x
        self.__y = y

    def get_id(self):
        return self.__id

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y