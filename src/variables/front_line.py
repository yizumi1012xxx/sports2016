# -*- coding: utf-8 -*-
"""
flont_line.py
"""

import numpy as np
import scipy.stats
from common.common import Util
from data.sports_dataset_frame import SportsDatasetFrame

class FrontLine:
    """
    FrontLine
    """

    def __init__(self):
        self.__sports_dataset_frame = None
        self.__match_status_id = None
        self.__home_players = []
        self.__home_players_x = []
        self.__home_players_y = []
        self.__home_attack_direction = None
        self.__away_players = []
        self.__away_players_x = []
        self.__away_players_y = []
        self.__away_attack_direction = None

    def __set_frame(self, frame: SportsDatasetFrame):
        self.__sports_dataset_frame = frame
        self.__match_status_id = self.__sports_dataset_frame.get_match_status_id()

        self.__home_players = self.__sports_dataset_frame.get_home_players()
        self.__home_players_x, self.__home_players_y =\
            self.__sports_dataset_frame.get_home_players_points()
        self.__home_attack_direction = self.__sports_dataset_frame.get_home_attack_direction()

        self.__away_players = self.__sports_dataset_frame.get_away_players()
        self.__away_players_x, self.__away_players_y =\
            self.__sports_dataset_frame.get_away_players_points()
        self.__away_attack_direction = self.__sports_dataset_frame.get_away_attack_direction()

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

        X0, Y0, Z0 = self.__calculate_kde(self.__away_players_x, self.__away_players_y)
        _, _, Z1 = self.__calculate_kde(self.__home_players_x, self.__home_players_y)
        flontLineX = []
        for y in range(len(Z0[0])):
            min_x, min_val = 0., 1.
            for x in range(len(Z0)):
                if Z0[x][y] > 0 and Z1[x][y] > 0 and abs(X0[x][y]) < 52.5 and abs(Y0[x][y]) < 41.5:
                    val = abs(Z0[x][y] - Z1[x][y]) / (Z0[x][y] + Z1[x][y])
                    if min_val > val:
                        min_x, min_val = X0[x][y], val
            flontLineX.append(min_x)
        return Util.ave(flontLineX)

    @staticmethod
    def __calculate_kde(x, y, bw_method=3.):

        # TODO refactor below parameter.
        IMAGE_X_MIN = -60
        IMAGE_X_MAX = 60
        IMAGE_Y_MIN = -40
        IMAGE_Y_MAX = 40

        X, Y = np.mgrid[IMAGE_X_MIN:IMAGE_X_MAX:106j, IMAGE_Y_MIN:IMAGE_Y_MAX:69j]
        positions = np.vstack([X.ravel(), Y.ravel()])
        values = np.vstack([np.array(x), np.array(y)])
        kernel = scipy.stats.gaussian_kde(values, bw_method)
        Z = np.reshape(kernel(positions).T, X.shape)
        return X, Y, Z