# -*- coding: utf-8 -*-
"""
This file get history_id from one frame data.
"""

from data.sports_dataset_frame import SportsDatasetFrame

class HistoryId:
    """
    HistoryId
    """

    def __init__(self):
        self.__sports_dataset_frame = None
        self.__match_status_id = None
        self.__history_id = None

    def __set_frame(self, frame: SportsDatasetFrame):
        self.__sports_dataset_frame = frame
        self.__match_status_id = self.__sports_dataset_frame.get_match_status_id()
        self.__history_id = self.__sports_dataset_frame.get_history_id()

    def get_name(self):
        """
        get_name
        """
        return self.__class__.__name__

    def get_value(self, frame: SportsDatasetFrame):
        """
        get_value
        """
        self.__set_frame(frame)
        return self.__history_id
