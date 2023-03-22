from pathlib import Path
from typing import List


def tail(filepath: Path, n: int) -> List[str]:
    """
    Similate Unix' "tail -n" command:
    - Read in the file ("filepath").
    - Parse it into a list of lines, stripping trailing newlines.
    - Return the last "n" lines.
    """
    with open(filepath, "r") as tail_file:
        lines = tail_file.readlines()

    lines = [ line.rstrip() for line in lines ]
    return lines[-n:]

