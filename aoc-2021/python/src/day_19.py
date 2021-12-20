import os
from dataclasses import dataclass, field
from typing import TextIO

import numpy as np
from parse import parse
from pyrr import Matrix33, Vector3


class ScannerMatched(Exception):
    pass


ROTATIONS = [
    Matrix33.from_eulers((0, 0, 0), dtype=np.int_),
    Matrix33.from_eulers((np.pi / 2, 0, 0), dtype=np.int_),
    Matrix33.from_eulers((np.pi, 0, 0), dtype=np.int_),
    Matrix33.from_eulers((3 * np.pi / 2, 0, 0), dtype=np.int_),
    Matrix33.from_eulers((0, 0, np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((np.pi / 2, 0, np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((np.pi, 0, np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((3 * np.pi / 2, 0, np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((0, 0, np.pi), dtype=np.int_),
    Matrix33.from_eulers((np.pi / 2, 0, np.pi), dtype=np.int_),
    Matrix33.from_eulers((np.pi, 0, np.pi), dtype=np.int_),
    Matrix33.from_eulers((3 * np.pi / 2, 0, np.pi), dtype=np.int_),
    Matrix33.from_eulers((0, 0, 3 * np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((np.pi / 2, 0, 3 * np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((np.pi, 0, 3 * np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((3 * np.pi / 2, 0, 3 * np.pi / 2), dtype=np.int_),
    Matrix33.from_eulers((0, np.pi / 2, 0), dtype=np.int_),
    Matrix33.from_eulers((np.pi / 2, np.pi / 2, 0), dtype=np.int_),
    Matrix33.from_eulers((np.pi, np.pi / 2, 0), dtype=np.int_),
    Matrix33.from_eulers((3 * np.pi / 2, np.pi / 2, 0), dtype=np.int_),
    Matrix33.from_eulers((0, 3 * np.pi / 2, 0), dtype=np.int_),
    Matrix33.from_eulers((np.pi / 2, 3 * np.pi / 2, 0), dtype=np.int_),
    Matrix33.from_eulers((np.pi, 3 * np.pi / 2, 0), dtype=np.int_),
    Matrix33.from_eulers((3 * np.pi / 2, 3 * np.pi / 2, 0), dtype=np.int_),
]


@dataclass
class Scanner:
    index: int
    beacons: list[Vector3]
    position: Vector3
    orientation: Matrix33
    done: bool = False
    rotated_beacons: dict[str, list[Vector3]] = field(default_factory=dict)

    def get_rotated_beacons(self, rot: Matrix33) -> list[Vector3]:
        key = repr(rot)
        if key not in self.rotated_beacons:
            self.rotated_beacons[key] = [rot * p for p in self.beacons]
        return self.rotated_beacons[key]


def parse_input(input_file: TextIO) -> list[Scanner]:
    scanners = []
    for line in input_file:
        line = line.strip()
        if line.startswith("---"):
            res = parse("--- scanner {idx:d} ---", line)
            scanner = Scanner(res.named["idx"], [], Vector3(), Matrix33.identity())
            scanners.append(scanner)
        elif line:
            scanner.beacons.append(
                Vector3([int(p) for p in line.split(",")], dtype=np.int_)
            )
    return scanners


def build_map(scanners: list[Scanner]) -> set[Vector3]:
    full_map = {tuple(b) for b in scanners[0].beacons}
    scanners[0].done = True
    while not all(scanner.done for scanner in scanners):
        try:
            for scanner in scanners:
                if scanner.done:
                    continue
                print("testing scanner", scanner.index)
                for rot in ROTATIONS:
                    rotated_beacons = scanner.get_rotated_beacons(rot)
                    for p1 in full_map:
                        for p2 in rotated_beacons:
                            offset = Vector3(p1) - p2
                            new_set = {tuple(p + offset) for p in rotated_beacons}
                            intersection = full_map.intersection(new_set)
                            if len(intersection) >= 12:
                                print(
                                    "matched scanner",
                                    scanner.index,
                                    "at position",
                                    offset,
                                    "and orientation",
                                    rot,
                                    "with matching beacons",
                                    intersection,
                                )
                                full_map.update(new_set)
                                scanner.orientation = rot
                                scanner.position = offset
                                scanner.done = True
                                raise ScannerMatched()
            else:
                raise RuntimeError("No match")
        except ScannerMatched:
            pass

    return full_map


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_19.in") as input_file:
        scanners = parse_input(input_file)

    full_map = build_map(scanners)
    print("part 1:", len(full_map))
