import os
from pathlib import Path

import config as cfg


def read_input(filepath):
    with open(filepath, "r") as fread:
        duration, num_intersections, num_streets, num_cars, bonus = map(int, fread.readline().strip().split(" "))
        var_dict = {
            'duration': duration,
            'num_inters': num_intersections,
            'num_streets': num_streets,
            'num_cars': num_cars,
            "bonus": bonus
        }

        lines = fread.read().splitlines()

        lines_street = lines[:num_streets]
        streets = []
        for line in lines_street:
            seps = line.split(" ")
            streets.append({
                "start_inter": int(seps[0]),
                "end_inter": int(seps[1]),
                "street_name": seps[2],
                "cost": int(seps[3])
            })

        lines_cars = lines[num_streets:]
        cars = []
        for line in lines_cars:
            seps = line.split(" ")
            cars.append({
                "num_streets": int(seps[0]),
                "streets": seps[1:]
            })

    return var_dict, streets, cars


if __name__ == "__main__":
    filepath = "inputs/a.txt"
    print(read_input(filepath))
