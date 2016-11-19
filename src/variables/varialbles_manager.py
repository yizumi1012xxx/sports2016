# -*- coding: utf-8 -*-
"""
variables_manager.py
"""

from common.common import File

class VariablesManager:
    """
    VariablesManager
    """

    def __init__(self):
        self.__variables = []

        self.__columns = []
        self.__rows = []

        self.__match_id = None
        self.__match_status_id = None

        self.__columns.append("MatchId")
        self.__columns.append("MatchStatusId")

    def add(self, cls):
        """
        add
        """
        self.__variables.append(cls)
        self.__columns.append(cls.get_name())

    def set_env(self, match_id, match_status_id):
        """
        set_env
        """
        self.__match_id = match_id
        self.__match_status_id = match_status_id

    def update(self, frame):
        """
        update
        """
        row = []
        row.append(self.__match_id)
        row.append(self.__match_status_id)
        for variable in self.__variables:
            row.append(variable.get_value(frame))
        self.__rows.append(row)

    def export(self, filepath):
        """
        export
        """
        File.write_csv(self.__columns, self.__rows, filepath)
