# -*- coding: utf-8 -*-
"""
util.py
"""

import numpy as np
import matplotlib.pyplot as plt

from common.common import Config, Path
from data.sports_dataset import SportsDataset

def draw(home_players_x, home_players_y, away_players_x, away_players_y, filename):
    """
    draw
    """
    axis = plt.figure().add_subplot(1, 1, 1)
    axis.scatter(home_players_x, home_players_y, c='red', label='home')
    axis.scatter(away_players_x, away_players_y, c='blue', label='away')
    axis.set_title(filename)
    axis.set_xlabel('x')
    axis.set_ylabel('y')
    axis.set_xlim(-60, 60)
    axis.set_ylim(-40, 40)
    axis.grid(True)
    axis.legend(loc='upper left')
    plt.savefig(Path.get_desktop_path() + filename + ".png")

def main():
    """
    main
    """
    for match in Config.load()["TRACKING_DATA_CONFIG"]:
        match_id = match["試合ID"]
        match_status_id = match["試合状態ID"]
        for frame in SportsDataset(match_id, match_status_id).get_frames():
            home_players_x, home_players_y = frame.get_home_players_points()
            away_players_x, away_players_y = frame.get_away_players_points()
            filename = "players[%s-%s-%s]" % (match_id, match_status_id, frame.get_frame_id())
            draw(home_players_x, home_players_y, away_players_x, away_players_y, filename)
            break

if __name__ == '__main__':
    main()
