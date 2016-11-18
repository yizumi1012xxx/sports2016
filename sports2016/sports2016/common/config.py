# -*- coding: utf-8 -*-
"""
config.py
"""
import common.file
import common.path

def load():
    """
    load
    """
    return common.file.read_json(common.path.get_abs_pass("../config.json"))
