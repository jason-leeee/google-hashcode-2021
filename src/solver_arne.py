import os
import sys
import math
import random
import numpy as np
import pandas as pd
from pathlib import Path

from heuristics import get_street_value

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
    """
    Args:
        arg 1: ???
        arg 2: ???

    Returns:
        ret: ???
    """

    inter_outgoings, inter_incomings = create_inters(var_dict, streets)

    # compute some features of the streets, car, ...
    street_occurs = stat_street_occurs(var_dict, streets, cars)
    street_costs = {street["street_name"]: street["cost"] for street in streets}
    # compute synthesised street values
    street_values = compute_street_values(streets, street_occurs, street_costs)

    # print some values, just to see
    street_values_sorted = sorted(list(street_values.items()), key=lambda e: e[1], reverse=True)
    #street_values_sorted = sorted([get_street_value(cars, streets, street, alpha=1) for street in streets])

    #print(street_values_sorted[:10])

    schedules = []
    for inter_id in range(var_dict["num_inters"]):
        street_outgoings = inter_outgoings[inter_id]
        street_incomings = inter_incomings[inter_id]

        green_lights = []

        subset_occurs = [street_occurs[street["street_name"]] for street in street_incomings]
        total_street_occurs = sum(subset_occurs)
        # we apply weighted street strategy only when the incoming streets are occuring in the car routes
        # if not, we can just set the duration of every incoming street to 1, they don't affect any results
        if total_street_occurs > 0:
            # compute the street values of all incoming streets
            incoming_values = [street_values[street["street_name"]] for street in street_incomings]
            incoming_values = [x for x in incoming_values if x != 0]
            min_value = min(incoming_values)
            for street in street_incomings:
                # duration = normalized value
                duration = math.floor(street_values[street["street_name"]] / min_value / len(incoming_values))
                if duration <= 0:
                    continue
                green_lights.append((street["street_name"], duration))
        else:
            # but why there are intersections without any cars passing?
            for street in street_incomings:
                green_lights.append((street["street_name"], 1))

        num_incoming_streets = len(green_lights)
        schedules.append((inter_id, num_incoming_streets, green_lights))

    return schedules
