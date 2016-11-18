# -*- coding: utf-8 -*-
"""
tracking.py
"""

import common.path
import common.file
import common.config
from data.tracking_frame_player import TrackingFramePlayer


class Tracking():
    """
    tracking dataを読み取りデータを保持するクラス。
    """

    FRAME_RATE = 25

    def __init__(self, match_id, match_status_id):
        self.__game_id = match_id
        self.__game_status_id = match_status_id
        self.__filepath = self.__get_file_path()
        self.__start_frame_id = None
        self.__data = []

        # load data
        _, data = common.file.read_csv(common.path.get_abs_pass(self.__filepath))
        for frame in data:
            if self.__start_frame_id is None:
                self.__start_frame_id = frame[0]
            for i in range(0, 29):
                self.__data.append(
                    TrackingFramePlayer(frame[0], frame[i*6+1], frame[i*6+2], frame[i*6+3],
                                        frame[i*6+4], frame[i*6+5], frame[i*6+6]))

    def __get_file_path(self):
        config = common.config.load()
        base_path = config["SPORTS_DATA_FOLDER_PATH"] + config["TRACKING_DATA_FOLDER_PATH"]
        for match_config in config["TRACKING_DATA_CONFIG"]:
            match_id = match_config["試合ID"]
            match_status_id = match_config["試合状態ID"]
            match_path = match_config["path"]
            if match_id == self.__game_id and match_status_id == self.__game_status_id:
                return base_path + match_path
        raise Exception("指定された試合ファイルが見つかりませんでした。")

    def find_tracking_frame_players(self, frame_id) -> [TrackingFramePlayer]:
        """
        find_tracking_frame
        """
        tracking_frame_players = []
        frame_id += self.__start_frame_id
        for tracking_frame_player in self.__data:
            if tracking_frame_player.get_frame_id() == frame_id:
                tracking_frame_players.append(tracking_frame_player)
        return tracking_frame_players
