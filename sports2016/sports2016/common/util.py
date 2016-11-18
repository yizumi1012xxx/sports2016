# -*- coding: utf-8 -*-
"""
util.py
"""
import common.file
import common.path
import common.config
import pandas as pd

def convert_uniform_number_to_player_id(match_id, is_home, uniform_number):
    """
    convert_uniform_number_to_player_id
    """
    if is_home:
        homeaway_f = 1
    else:
        homeaway_f = 2

    config = common.config.load()
    player_list_path = \
        config["SPORTS_DATA_FOLDER_PATH"] +\
        config["BALL_TOUCH_DATA_FOLDER_PATH"] +\
        config["BALL_TOUCH_PLAYER_LIST_PATH"]
    
    dataframe = pd.read_csv(common.path.get_abs_pass(player_list_path), encoding='Shift_JIS')
    columns = dataframe.columns.tolist()
    rows = dataframe.values

    for row in rows:
        _homeaway_f = row[columns.index("ホームアウェイF")]
        _match_id = row[columns.index("試合ID")]
        _uniform_number = row[columns.index("背番号")]
        _player_id = row[columns.index("選手ID")]

        if _homeaway_f == homeaway_f\
            and _match_id == match_id\
            and _uniform_number == uniform_number:
            return _player_id
