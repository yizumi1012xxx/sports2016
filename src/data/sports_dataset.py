# -*- coding: utf-8 -*-
"""
sports_dataset.py
"""

from data.ball_touch import BallTouchCustom
from data.tracking import Tracking
from data.sports_dataset_frame import SportsDatasetFrame
from data.sports_dataset_frame_player import SportsDatasetFramePlayer
from data.player_list import PlayerList

class SportsDataset():
    """
    SportsDataset
    """

    def __init__(self, match_id: float, match_status_id: float):
        print("Initalize SportsDataset.")
        self.__match_id = int(match_id)
        self.__match_status_id = int(match_status_id)
        self.__ball_touch = BallTouchCustom(self.__match_id, self.__match_status_id)
        self.__tracking = Tracking(self.__match_id, self.__match_status_id)
        self.__player_list = PlayerList()
        self.__frames = []
        self.__get_frames()

    def __get_frames(self) -> None:
        for frame in self.__ball_touch.get_frames():
            # ball_touch frame
            frame_id = frame.get_frame_id()
            history_id = frame.get_history_id()
            ball_x = frame.get_ball_x()
            ball_y = frame.get_ball_y()
            #attacker_is_home = frame.is_home()
            ball_player_id = frame.get_player_id()
            ball_player = None
            home_players = []
            away_players = []

            print("loading...[%s-%s-%s]" % (self.__match_id, self.__match_status_id, frame_id))
            # tracking frame
            for player in self.__tracking.find_tracking_frame_players(frame_id):
                try:
                    player_x = player.get_point_x()
                    player_y = player.get_point_y()
                    player_is_home = player.is_home()
                    player_uniform_number = player.get_uniform_number()
                    player_id = self.__player_list.get_player_id(
                        self.__match_id, player_is_home, player_uniform_number)

                    sports_dataset_frame_player = SportsDatasetFramePlayer(
                        player_id, player_is_home, player_x, player_y)

                    if player_is_home:
                        home_players.append(sports_dataset_frame_player)
                    else:
                        away_players.append(sports_dataset_frame_player)

                    if ball_player_id == player_id:
                        ball_player = sports_dataset_frame_player
                except ValueError:
                    # player_idなどが適切に取得できない場合はスキップする。（審判・不明など）
                    pass

            self.__frames.append(SportsDatasetFrame(
                self.__match_status_id, frame_id, history_id, ball_x, ball_y,
                ball_player, home_players, away_players))

    def get_frames(self) -> [SportsDatasetFrame]:
        """
        get_frames
        """
        return self.__frames
