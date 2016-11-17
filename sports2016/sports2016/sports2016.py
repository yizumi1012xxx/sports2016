# -*- coding: utf-8 -*-

import common.path as path
import common.file as file
import common.flag as flag
from data.tracking import Trackings

# 1. 全てのゲーム分のトラッキングデータを読み込む。　-> 1個ずつ読み込むようにする
tracking_path = path.get_home_path() + "/GoogleDrive/sports2016/data(password無し)/16~17コンペ_サッカー（トラッキング）_08"
tracking_data_config = [
    {"path": tracking_path + "/2016022701_磐田vs名古屋_前半_08.csv", "試合ID": 2016022701, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022701_磐田vs名古屋_後半_08.csv", "試合ID": 2016022701, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022702_広島vs川崎F_前半_08.csv", "試合ID": 2016022702, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022702_広島vs川崎F_後半_08.csv", "試合ID": 2016022702, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022703_鳥栖vs福岡_前半_08.csv", "試合ID": 2016022703, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022703_鳥栖vs福岡_後半_08.csv", "試合ID": 2016022703, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022704_柏vs浦和_前半_08", "試合ID": 2016022704, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022704_柏vs浦和_後半_08", "試合ID": 2016022704, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022705_湘南vs新潟_前半_08", "試合ID": 2016022705, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022705_湘南vs新潟_後半_08", "試合ID": 2016022705, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022706_神戸vs甲府_前半_08", "試合ID": 2016022706, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022706_神戸vs甲府_後半_08", "試合ID": 2016022706, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022707_横浜FMvs仙台_前半_08", "試合ID": 2016022707, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022707_横浜FMvs仙台_後半_08", "試合ID": 2016022707, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022708_FC東京vs大宮_前半_08", "試合ID": 2016022708, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022708_FC東京vs大宮_後半_08", "試合ID": 2016022708, "試合状態ID": 2},
    #{"path": tracking_path + "/2016022801_G大阪vs鹿島_前半_08", "試合ID": 2016022801, "試合状態ID": 1},
    #{"path": tracking_path + "/2016022801_G大阪vs鹿島_後半_08", "試合ID": 2016022801, "試合状態ID": 2},
]
trackings = Trackings(tracking_data_config)


### 2. 全てのゲーム分のボールタッチデータを読み込む。 -> 神谷さんから頂いたボールタッチデータを読み込む。
ball_touch_path = "/GoogleDrive/sports2016/data/data4LDA_action.csv"
header, datas = file.read_csv(path.get_home_path() + ball_touch_path)
print(header)
for data in datas:
    match_id = data[header.index("matchID")]
    match_state = data[header.index("matchState")]
    attack_no = data[header.index("attackNo")]
    frame_id = data[header.index("frameID")]
    
    history_id = data[header.index("historyID")]
    team_id = data[header.index("teamID")]
    player_id = data[header.index("playerID")]          # タッチプレイヤーID
    homeaway = data[header.index("homeaway")]           # ballタッチプレイヤーがhome or away
    ball_x = data[header.index("ballX")]
    ball_y = data[header.index("ballY")]

# 3. ボールタッチデータの絶対時間，試合ID，試合状態IDの３つのパラメータが固定した際に以下の処理を行う。
#   1. ボールタッチデータから，チームIDを取得する。
#   2. ボールタッチデータから，ボールの座標を取得する。
#   3. トラッキングデータから，1で取得したチームIDを基にボールタッチしているチームメンバーの座標，ボールタッチしていないチームメンバーの座標を取得する。
#   4. 1,2,3で得た情報から，各種変数を算出する。
#       - 入力：ボール座標，ボールタッチしているチーム（HOME or AWAY），HOMEチームプレイヤー座標，AWAYチームプレイヤー座標，前半or後半

# 4. 得られた変数ごとに以下のような形式で出力する。
#   試合ID, 試合状態ID, 絶対時間, アクションID, 攻撃番号 | 