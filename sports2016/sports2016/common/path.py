# -*- coding: utf-8 -*-

import os

def get_desktop_path():
    return os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/"

def get_abs_pass(filepath):
    return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath))

def get_file_name(filepath):
    fileName, ext = os.path.splitext(os.path.basename(filepath))
    return fileName

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