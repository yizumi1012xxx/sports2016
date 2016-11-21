# -*- coding: utf-8 -*-
"""
sports2016.py
"""

from common.common import Config, Path
from data.sports_dataset import SportsDataset
from variables.varialbles_manager import VariablesManager
from variables.compactness_home import CompactnessHome
from variables.compactness_away import CompactnessAway
from variables.defense_vulnerability_away import DefenseVulnerabilityAway
from variables.defense_vulnerability_home import DefenseVulnerabilityHome
from variables.offside_line_away import OffsideLineAway
from variables.offside_line_home import OffsideLineHome
from variables.front_line import FrontLine
from variables.history_id import HistoryId
from variables.neighbor_player_of_before import NeighborPlayerOfBefore
from variables.neighbor_player_of_behind import NeighborPlayerOfBehind
from variables.neighbor_player_of_left import NeighborPlayerOfLeft
from variables.neighbor_player_of_right import NeighborPlayerOfRight

def main():
    """
    main
    """
    var = VariablesManager()
    var.add(HistoryId())
    var.add(CompactnessAway())
    var.add(CompactnessHome())
    var.add(DefenseVulnerabilityAway())
    var.add(DefenseVulnerabilityHome())
    var.add(OffsideLineAway())
    var.add(OffsideLineHome())
    var.add(FrontLine())
    var.add(NeighborPlayerOfBefore())
    var.add(NeighborPlayerOfBehind())
    var.add(NeighborPlayerOfLeft())
    var.add(NeighborPlayerOfRight())

    for match in Config.load()["TRACKING_DATA_CONFIG"]:
        match_id = match["試合ID"]
        match_status_id = match["試合状態ID"]
        var.set_env(match_id, match_status_id)
        for frame in SportsDataset(match_id, match_status_id).get_frames():
            print("analizing...[%s-%s-%s]" % (match_id, match_status_id, frame.get_frame_id()))
            var.update(frame)
        break

    var.export(Path.get_desktop_path() + "output.csv")

if __name__ == '__main__':
    main()
