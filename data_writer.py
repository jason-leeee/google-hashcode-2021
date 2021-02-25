import os
from pathlib import Path

import config as cfg


def write_output(filepath, output_data):
    """
    Args:
        filepath: full relative path of the output text file, e.g. "outputs/sample.txt".
        output_data: a list of sth, tuples?
    """

    output_lines = []
    for __TODO__ in output_data:

        line = __TODO__

        line += "\n"
        output_lines.append(line)
    
    with open(filepath, "w") as fwrite:
        fwrite.writelines(output_lines)


if __name__ == "__main__":
    filepath = "outputs/sample.txt"
    test_data = __TODO__
    write_output(filepath, test_data)
