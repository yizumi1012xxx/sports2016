# -*- coding: utf-8 -*-
"""
common.py
"""
import codecs
import csv
import json
import os
import pandas as pd


class Util:
    """
    Util
    """

    @staticmethod
    def max2(data_array):
        """
        配列から2番目に大きい値を取得
        """
        return sorted(data_array)[-2]

    @staticmethod
    def min2(data_array):
        """
        配列から2番目に小さい値を取得
        """
        return sorted(data_array)[1]

    @staticmethod
    def ave(data_array):
        """
        配列から平均値を取得
        """
        return float(sum(data_array)) /float(len(data_array))


class Path:
    """
    Path
    """

    @staticmethod
    def get_desktop_path():
        """
        get_desktop_path
        """
        return os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "/Desktop/"

    @staticmethod
    def get_abs_pass(filepath):
        """
        get_abs_pass
        """
        return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath))

    @staticmethod
    def get_file_name(filepath):
        """
        get_file_name
        """
        fileName, ext = os.path.splitext(os.path.basename(filepath))
        return fileName


class Config:
    """
    Config
    """

    @staticmethod
    def load():
        """
        load
        """
        return File.read_json(Path.get_abs_pass("../config.json"))


class File:
    """
    File
    """

    @staticmethod
    def read_csv(filepath):
        """
        read_csv
        """
        dataframe = pd.read_csv(filepath, encoding='Shift_JIS', dtype='str')
        return dataframe.columns.tolist(), dataframe.values

    @staticmethod
    def write_csv(header, data, filepath):
        """
        write_csv
        """
        with open(filepath, 'w') as file_object:
            writer = csv.writer(file_object, lineterminator='\n')
            writer.writerow(header)
            writer.writerows(data)

    @staticmethod
    def read_json(filepath):
        """
        read_json
        """
        with codecs.open(filepath, "r", "utf-8") as file_object:
            return json.loads(file_object.read())
