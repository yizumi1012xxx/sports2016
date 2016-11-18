# -*- coding: utf-8 -*-

import common.path as path
import common.file as file
import common.flag as flag


class Tracking():
    """
    tracking dataを読み取りデータを保持するクラス。
    """
    FRAME_RATE = 25

    def __init__(self, filepath, game_id, game_status_id):

        self.filepath = filepath
        self.game_id = game_id
        self.game_status_id = game_status_id
        self.start_frame_id = None
        self.data = []

        self.__get_data_from_csv()

    def get_id(self):
        """
        game_idとgame_status_idを取得
        """
        return self.game_id, self.game_status_id

    def __get_data_from_csv(self):
        header, data = file.read_csv(path.get_abs_pass(self.filepath))
        for index, frame in enumerate(data):
            if(self.start_frame_id == None):
                self.start_frame_id = frame[0]
            tf = TrackingFrame(frame[0])
            for i in range(0,29):
                tf.add(frame[i*6+1], frame[i*6+2], frame[i*6+3], frame[i*6+4], frame[i*6+5], frame[i*6+6])
            self.add(tf)

    def add(self, tracking_frame):
        self.data.append(tracking_frame)

    def find_tracking_frame_by_elapsed_time(self, elapsed_seconds):
        """
        試合経過時間から最も近いフレームを探し，TrackingFrameを返す
        elapsed_seconds: 経過時間[秒]
        """
        frame = elapsed_seconds * self.FRAME_RATE + self.start_frame_id
        return self.find_tracking_frame_by_frame_id(frame)
    
    def find_tracking_frame_by_frame_id(self, frame_id):
        for frame in self.data:
            if(frame.get_frame_id() == frame_id):
                return frame
        raise Exception("frameIdが不正です。")

    def find_tracking_frame_home_player_by_elapsed_time(self, elapsed_seconds):
        frame_id = elapsed_seconds * self.FRAME_RATE + self.start_frame_id
        frame = self.find_tracking_frame_by_frame_id(frame_id)
        return TrackingFrameHomePlayer(frame)

    def find_tracking_frame_away_player_by_elapsed_time(self, elapsed_seconds):
        frame_id = elapsed_seconds * self.FRAME_RATE + self.start_frame_id
        frame = self.find_tracking_frame_by_frame_id(frame_id)
        return TrackingFrameAwayPlayer(frame)


class TrackingFrame():

    def __init__(self, frame_id):
        self.frame_id = frame_id
        self.data = []

    def get_frame_id(self):
        return self.frame_id

    def get_players(self):
        return self.data

    def add(self, team_id, system_target_id, uniform_number, point_x, point_y, velocity):
        player = TrackingFramePlayer(team_id, system_target_id, uniform_number, point_x, point_y, velocity)
        self.data.append(player)

class TrackingFrameHomePlayer():

    def __init__(self, tracking_frame):
        self.tracking_frame = tracking_frame
        self.data = []

        for player in self.tracking_frame.get_players():
            if player.get_team_id() == flag.HOME:
                self.add(player)

    def add(self, player):
        self.data.append(player)


class TrackingFrameAwayPlayer():

    def __init__(self, tracking_frame):
        self.tracking_frame = tracking_frame
        self.data = []

        for player in self.tracking_frame.get_players():
            if player.get_team_id() == flag.AWAY:
                self.add(player)

    def add(self, player):
        self.data.append(player)


class TrackingFramePlayer():
    
    def __init__(self, team_id, system_target_id, uniform_number, point_x, point_y, velocity):
        self.team_id = team_id
        self.system_target_id = system_target_id
        self.uniform_number = uniform_number
        self.point_x = point_x
        self.point_y = point_y
        self.velocity = velocity

    def get_team_id(self):
        return self.team_id

    def get_uniform_number(self):
        return self.uniform_number

    def get_point_x_cm(self):
        return self.point_x

    def get_point_y_cm(self):
        return self.point_y

    def get_point_x_m(self):
        return self.point_x / 100.

    def get_point_y_m(self):
        return self.point_y / 100.

    
class Trackings():
    
    def __init__(self, config: dict) -> None:
        self.data = []
        for c in config:
            file_path = c["path"]
            game_id = c["試合ID"]
            game_status_id = c["試合状態ID"]
            tracking = Tracking(file_path, game_id, game_status_id)
            self.add(tracking)

    def add(self, tracking: Tracking) -> None:
        self.data.append(tracking)

    def get_trackings(self) -> [Tracking]:
        return self.data

    def find_tracking_by_id(self, game_id: int, game_status_id: int) -> Tracking:
        for tracking in self.get_trackings():
            _game_id, _game_status_id = tracking.get_id()
            if(game_id == _game_id and game_status_id == _game_status_id):
                return tracking
        raise Exception("game_idまたはgame_status_idが不正です。")
