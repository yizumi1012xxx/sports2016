# -*- coding: utf-8 -*-
"""
This is the entry point code of sports contenst 2016.
"""
import json
import codecs
import common.path as path

from data.tracking import Tracking
from data.ball_touch import BallTouchCustom

def load_config():
    """
    Load config from config.json
    """
    config_filepath = "./config.json"
    with codecs.open(config_filepath, "r", "utf-8") as config_file:
        return json.loads(config_file.read())


# 1. config読み込み
CONFIG = load_config()

# 2. 全試合のボールタッチデータを取得
ALL_BALL_TOUCH_DATA = BallTouchCustom(CONFIG["BALL_TOUCH_DATA_PATH"])

# 3. 試合ごとにfor文でループ
for match in CONFIG["TRACKING_DATA_CONFIG"]:
    MATCH_FILEPATH = match["path"]
    MATCH_ID = match["試合ID"]
    MATCH_STATUS_ID = match["試合状態ID"]
    # 3-1. 1ゲーム分のトラッキングデータを読み込む。
    TRACKING_DATA = Tracking(MATCH_FILEPATH, MATCH_ID, MATCH_STATUS_ID)
    # 2. 1ゲーム分のボールタッチデータを読み込む。（神谷さんから頂いたボールタッチデータを読み込む。）
    BALL_TOUCH_DATA = ALL_BALL_TOUCH_DATA.get_match_actions(MATCH_ID, MATCH_STATUS_ID)
    # 3. ボールタッチデータの絶対時間，試合ID，試合状態IDの３つのパラメータが固定した際に以下の処理を行う。
    #   1. ボールタッチデータから，チームIDを取得する。
    #   2. ボールタッチデータから，ボールの座標を取得する。
    #   3. トラッキングデータから，1で取得したチームIDを基にボールタッチしているチームメンバーの座標，ボールタッチしていないチームメンバーの座標を取得する。
    #   4. 1,2,3で得た情報から，各種変数を算出する。
    #       - 入力：ボール座標，ボールタッチしているチーム（HOME or AWAY），HOMEチームプレイヤー座標，AWAYチームプレイヤー座標，前半or後半
    # 4. 得られた変数ごとに以下のような形式で出力する。
    #   試合ID, 試合状態ID, 絶対時間, アクションID, 攻撃番号 |
