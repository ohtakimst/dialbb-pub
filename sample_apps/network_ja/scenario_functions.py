#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# scenario_functions.py
#   functions used in sample Japanese app

__version__ = '0.1'
__author__ = 'Mikio Nakano'
__copyright__ = 'C4A Research Institute, Inc.'

from typing import Dict, Any

known_ramens = ("豚骨ラーメン", "味噌ラーメン", "塩ラーメン", "醤油ラーメン")

def is_known_ramen(ramen: str, context: Dict[str, Any]) -> bool:
    return ramen in known_ramens


def is_novel_sandwich(ramen: str, context: Dict[str, Any]) -> bool:
    return ramen not in known_ramens


ramen_map = {"豚骨ラーメン": "博多",
             "味噌ラーメン": "札幌",
             "塩ラーメン": "函館",
             "醤油ラーメン": "東京"}


def get_ramen_location(ramen: str, variable: str, context: Dict[str, Any]) -> None:
    location:str = ramen_map.get(ramen, "日本")
    context[variable] = location






