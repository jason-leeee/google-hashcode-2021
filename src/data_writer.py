import os
from pathlib import Path

import config as cfg


def write_output(filepath, schedules):
    """
    Args:
        filepath: full relative path of the output text file, e.g. "outputs/sample.txt".
        schedules: a list of tuple (inter_id, num_incoming_streets, green_lights)
            - inter_id (int): intersection id
            - num_incoming_streets (int): number of incoming streets
            - green_lights (list of tuple (street_name, duration)): green light control schedule, i.e. which street is green for how long
                - street_name (str): street name
                - duration (int): how long each street will have a green light
    """

    output_lines = [str(len(schedules)) + "\n"]
    for inter_id, num_incoming_streets, green_lights in schedules:
        output_lines.append(str(inter_id) + "\n")
        output_lines.append(str(num_incoming_streets) + "\n")
        for street_name, green_duration in green_lights:
            output_lines.append(street_name + " " + str(green_duration) + "\n")
    
    with open(filepath, "w") as fwrite:
        fwrite.writelines(output_lines)


if __name__ == "__main__":
    filepath = "outputs/sample.txt"
    schedules = [
        (
            1,
            2,
            [
                ("rue-d-athenes", 2),
                ("rue-d-amsterdam", 1),
            ]
        ),
        (
            0,
            1,
            [
                ("rue-de-londres", 2),
            ]
        ),
        (
            2,
            1,
            [
                ("rue-de-moscou", 1),
            ]
        )
    ]
    write_output(filepath, schedules)
