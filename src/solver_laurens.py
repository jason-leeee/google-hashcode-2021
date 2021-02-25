import os
import sys
import math
import random
import numpy as np
import pandas as pd
from pathlib import Path

import config as cfg
from helper import *
from collections import defaultdict


def create_inters(var_dict, streets):
    inter_outgoings = {inter_id: [] for inter_id in range(var_dict["num_inters"])}
    inter_incomings = {inter_id: [] for inter_id in range(var_dict["num_inters"])}
    for street in streets:
        inter_outgoings[street["start_inter"]].append(street)
        inter_incomings[street["end_inter"]].append(street)
    return inter_outgoings, inter_incomings


def solve(var_dict, streets, cars):
    inter_outgoings, inter_incomings = create_inters(var_dict, streets)
    street_dict = defaultdict(int)

    for car in cars:
        for street in car['streets']:
            street_dict[street] += 1
    
    schedules = []
    for inter_id in range(var_dict["num_inters"]):
        huil = False
        street_outgoings = inter_outgoings[inter_id]
        street_incomings = inter_incomings[inter_id]

        num_incoming_streets = len(street_incomings)
        green_lights = []
        
        street_importance = []
        for street in street_incomings:
            street_importance.append(street_dict[street['street_name']])
        
        if len(street_importance) > 7:
            huil = True
            
        street_importance = list(set(street_importance))
        street_importance.sort()
        for street in street_incomings:
            if street_dict[street['street_name']] != 0:
                index = street_importance.index(street_dict[street['street_name']])
                if huil:
                    green_lights.append((street["street_name"], 1))
                else:
                    green_lights.append((street["street_name"], index + 1))
        if len(green_lights) > 0:
            schedules.append((inter_id, len(green_lights), green_lights))
    return schedules
