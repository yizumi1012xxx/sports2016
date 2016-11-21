# -*- coding: utf-8 -*-
"""
tracking.py
"""

from common.common import Config, File, Path
from data.tracking_frame_player import TrackingFramePlayer


class Tracking():
    """
    Tracking
    """

    FRAME_RATE = 25

    def __init__(self, match_id: int, match_status_id: int):
        self.__game_id = match_id
        self.__game_status_id = match_status_id
        self.__filepath = self.__get_file_path()
        self.__frames = []
        self.__start_frame_id = None
        self.__load()

    def __get_file_path(self) -> str:
        config = Config.load()
        base_path = config["SPORTS_DATA_FOLDER_PATH"] + config["TRACKING_DATA_FOLDER_PATH"]
        for match_config in config["TRACKING_DATA_CONFIG"]:
            match_id = int(match_config["試合ID"])
            match_status_id = int(match_config["試合状態ID"])
            match_path = match_config["path"]
            if match_id == self.__game_id and match_status_id == self.__game_status_id:
                return Path.get_abs_pass(base_path + match_path)
        raise IOError("指定された試合ファイルが見つかりませんでした。")

    def __load(self) -> None:
        _, data = File.read_csv(Path.get_abs_pass(self.__filepath))
        for frame in data:
            if self.__start_frame_id is None:
                self.__start_frame_id = int(frame[0])
            self.__frames.append(frame)

    def find_tracking_frame_players(self, require_frame_id: int) -> [TrackingFramePlayer]:
        """
        find_tracking_frame
        """
        require_frame_id += self.__start_frame_id
        require_frame_id = self.__find_near_tracking_frame_id(require_frame_id)
        for frame in self.__frames:
            frame_id = int(frame[0])
            if frame_id == require_frame_id:
                tracking_frame_players = []
                for i in range(0, 29):
                    team_id = int(frame[i*6+1])
                    system_target_id = int(frame[i*6+2])
                    uniform_number = int(frame[i*6+3])
                    point_x = float(frame[i*6+4])
                    point_y = float(frame[i*6+5])
                    velocity = float(frame[i*6+6])
                    tracking_frame_players.append(TrackingFramePlayer(
                        frame_id, team_id, system_target_id, uniform_number,
                        point_x, point_y, velocity))
                return tracking_frame_players

    def __find_near_tracking_frame_id(self, require_frame_id: int) -> int:
        """
        find_near_tracking_frame_id
        """
        near_frame_id = None
        for frame in self.__frames:
            _frame_id = int(frame[0])
            if require_frame_id == _frame_id:
                return require_frame_id
            if near_frame_id is None:
                near_frame_id = _frame_id
            elif abs(near_frame_id - require_frame_id) > abs(_frame_id - require_frame_id):
                near_frame_id = _frame_id
        return near_frame_id
