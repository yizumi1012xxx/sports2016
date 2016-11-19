# -*- coding: utf-8 -*-
"""
util.py
"""

def max2(data_array):
    """
    配列から2番目に大きい値を取得
    """
    return sorted(data_array)[-2]

def min2(data_array):
    """
    配列から2番目に小さい値を取得
    """
    return sorted(data_array)[1]

def ave(data_array):
    """
    配列から平均値を取得
    """
    return float(sum(data_array)) /float(len(data_array))
