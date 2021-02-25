import os
import sys
import math
import random
import numpy as np
import pandas as pd
from pathlib import Path

import config as cfg
from helper import *


def create_inters(var_dict, streets):
    inter_outgoings = {inter_id: [] for inter_id in range(var_dict["num_inters"])}
    inter_incomings = {inter_id: [] for inter_id in range(var_dict["num_inters"])}
    for street in streets:
        inter_outgoings[street["start_inter"]].append(street)
        inter_incomings[street["end_inter"]].append(street)
    return inter_outgoings, inter_incomings


def stat_street_occurs(var_dict, streets, cars):
    street_occurs = {street["street_name"]: 0 for street in streets}

    for car in cars:
        for street_name in car["streets"]:
            street_occurs[street_name] += 1

    return street_occurs


def compute_street_values(streets, street_occurs, street_costs):
    street_values = {}
    for street in streets:
        occur = street_occurs[street["street_name"]]
        cost = street_costs[street["street_name"]]
        value = occur / cost
        street_values[street["street_name"]] = value
    return street_values


def solve(var_dict, streets, cars):
    inter_outgoings, inter_incomings = create_inters(var_dict, streets)

    # add a street id, starting from 1
    streets = [{"street_id": i + 1, **items} for i, items in enumerate(streets.items())]
    street_hash = {street["street_name"]: street for street in streets}

    schedules = {
        {
            "timetable": np.zeros(var_dict["duration"], dtype=np.int16)
        }
        for inter_id in range(var_dict["num_inters"])
    }

    for car in cars:
        # add this car
        t = 0
        delay = 0
        for street_name in car["streets"][1:]:
            street = street_hash[street_name]
            inter_start = street["start_inter"]
            inter_end = street["end_inter"]


            t += street["cost"] + delay

            inter_car = street["end_inter"]
            
            schedule = schedules[inter_car]
            timetable = schedule["timetable"]
            if timetable[t] == 0:
                timetable[t] = street["street_id"]
                delay = 0
            else:
                # this car will be delayed
                delay = 0

    return schedules
