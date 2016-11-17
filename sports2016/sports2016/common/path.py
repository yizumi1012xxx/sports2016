# -*- coding: utf-8 -*-

import os

_HOMEPATH   = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH")
_SRCPATH    = _HOMEPATH + "/Desktop/sports/data/"
_DSTPATH    = _HOMEPATH + "/Desktop/sports/output/"
FIELD_WIDTH, FIELD_HEIGHT = 105., 68.
IMAGE_X_MIN, IMAGE_X_MAX, IMAGE_Y_MIN, IMAGE_Y_MAX = -60, 60, -40, 40
    
GAMES = ['20150314_1', '20150314_2', '20150627_1', '20150627_2']

def get_home_path():
    return _HOMEPATH

def get_team_name(teamId):
    if teamId == HOME:
        return 'HOME'
    elif teamId == AWAY:
        return 'AWAY'

def make_dst_folder():
    if not os.path.exists(_DSTPATH):
        os.mkdir(_DSTPATH)
    return

def get_abs_pass(filepath):
    return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath))

def get_file_name(filepath):
    fileName, ext = os.path.splitext(os.path.basename(filepath))
    return fileName

def get_player_tracking_filepath(name):
    return _SRCPATH + 'player_tracking/' + name + '.csv'

def get_ball_tracking_filepath(name):
    return _SRCPATH + 'ball_tracking/' + name + '.csv'

def get_output_filepath(name):
    return _DSTPATH + 'output(' + name + ').csv'

def get_output_image_path(name):
    return _DSTPATH + name +'.png'

def max2(dataArray):
    return sorted(dataArray)[-2]

def min2(dataArray):
    return sorted(dataArray)[1]

def ave(dataArray):
    return float(sum(dataArray)) /float(len(dataArray))

def count_array(dataArray):
    all, target = 0., 0.
    for _dataArray in dataArray:
        for _data in _dataArray:
            all += 1.
            if _data == 1:
                target += 1.
    return target / all