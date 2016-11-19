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
        self.__data = []
        self.__start_frame_id = None
        self.__load()

    def __get_file_path(self):
        config = common.config.load()
        base_path = config["SPORTS_DATA_FOLDER_PATH"] + config["TRACKING_DATA_FOLDER_PATH"]
        for match_config in config["TRACKING_DATA_CONFIG"]:
            match_id = int(match_config["試合ID"])
            match_status_id = int(match_config["試合状態ID"])
            match_path = match_config["path"]
            if match_id == self.__game_id and match_status_id == self.__game_status_id:
                return common.path.get_abs_pass(base_path + match_path)
        raise IOError("指定された試合ファイルが見つかりませんでした。")

    def __load(self):
        _, data = common.file.read_csv(common.path.get_abs_pass(self.__filepath))
        for frame in data:
            # 初期フレームを登録
            if self.__start_frame_id is None:
                self.__start_frame_id = int(frame[0])
            # データを保存
            self.__data.append(frame)

    def find_tracking_frame_players(self, frame_id) -> [TrackingFramePlayer]:
        """
        find_tracking_frame
        """
        frame_id += self.__start_frame_id
        frame_id = self.__find_near_tracking_frame_id(frame_id)
        for frame in self.__data:
            if int(frame[0]) == frame_id:
                tracking_frame_players = []
                for i in range(0, 29):
                    tracking_frame_players.append(
                        TrackingFramePlayer(frame[0], frame[i*6+1], frame[i*6+2], frame[i*6+3],
                                            frame[i*6+4], frame[i*6+5], frame[i*6+6]))
                return tracking_frame_players

    def __find_near_tracking_frame_id(self, require_frame_id):
        """
        find_near_tracking_frame_id
        """
        near_frame_id = None
        for frame in self.__data:
            _frame_id = int(frame[0])
            if require_frame_id == _frame_id:
                return require_frame_id
            if near_frame_id is None:
                near_frame_id = _frame_id
            elif abs(near_frame_id - require_frame_id) > abs(_frame_id - require_frame_id):
                near_frame_id = _frame_id
        return near_frame_id
