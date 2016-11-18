# -*- coding: utf-8 -*-
"""
This is the entry point code of sports contenst 2016.
"""
import common.file
import common.path
import common.config

from data.sports_dataset import SportsDataset

# 1. config読み込み
# 2. 試合ごとにfor文でループ
for match in common.config.load()["TRACKING_DATA_CONFIG"]:
    MATCH_ID = match["試合ID"]
    MATCH_STATUS_ID = match["試合状態ID"]
    print("Load match : %s (%s)" % (MATCH_ID, MATCH_STATUS_ID))
    # 2-1. 1ゲーム分のトラッキングデータを読み込む。
    # 2-2. 1ゲーム分のボールタッチデータを読み込む。（神谷さんから頂いたボールタッチデータを読み込む。）
    # 2-3. 1ゲーム分のトラッキングデータとボールタッチデータを統合。
    SPORTS_DATASET = SportsDataset(MATCH_ID, MATCH_STATUS_ID)
    # 2-4. アクション発生フレームをfor文でループ
    for frame in SPORTS_DATASET.get_frames():
        # 2-4-1. 必要データ取得
        frame_id = frame.get_frame_id()
        ball_x = frame.get_ball_x()
        ball_y = frame.get_ball_y()
        attack_player = frame.get_attack_player()
        attack_team_players = frame.get_attack_team_players()
        defence_team_players = frame.get_defence_team_players()
        # 2-4-2. 変数を作成
