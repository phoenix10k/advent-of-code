import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Packet:
    version: int
    packet_id: int
    literal_value: Optional[int]
    children: list["Packet"]

    @classmethod
    def from_bin_str(cls, bin_str: str) -> tuple["Packet", str]:
        literal_value: Optional[int] = None
        children: list["Packet"] = []

        version = int(bin_str[:3], base=2)
        bin_str = bin_str[3:]
        packet_id = int(bin_str[:3], base=2)
        bin_str = bin_str[3:]
        if packet_id == 4:
            bits = ""
            while True:
                more_bit = bin_str[0]
                bits += bin_str[1:5]
                bin_str = bin_str[5:]
                if more_bit == "0":
                    break
            literal_value = int(bits, base=2)
        else:
            len_type = bin_str[0]
            bin_str = bin_str[1:]
            if len_type == "0":
                length = int(bin_str[:15], base=2)
                bin_str = bin_str[15:]
            else:
                length = int(bin_str[:11], base=2)
                bin_str = bin_str[11:]
            start_len = len(bin_str)
            while True:
                child, bin_str = cls.from_bin_str(bin_str)
                children.append(child)
                if len_type == "0":
                    if start_len - len(bin_str) >= length:
                        break
                else:
                    if len(children) >= length:
                        break

        return cls(version, packet_id, literal_value, children), bin_str

    def sum_versions(self) -> int:
        return self.version + sum(child.sum_versions() for child in self.children)


def hex2bin(input_hex_string: str) -> str:
    return "".join(f"{int(c, base=16):04b}" for c in input_hex_string)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_16.in") as input_file:
        bin_string = hex2bin(next(input_file).strip())

    root, rest = Packet.from_bin_str(bin_string)
    print("part 1:", root.sum_versions())
