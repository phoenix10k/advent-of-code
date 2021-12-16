import os

import pytest
from day_16 import Packet, hex2bin


def test_part_0a() -> None:
    bin_str = hex2bin("D2FE28")
    assert bin_str == "110100101111111000101000"

    packet, rest = Packet.from_bin_str(bin_str)
    assert packet.version == 6
    assert packet.packet_id == 4
    assert packet.literal_value == 2021
    assert packet.children == []
    assert rest == "000"

def test_part_0b() -> None:
    bin_str = hex2bin("38006F45291200")
    assert bin_str == "00111000000000000110111101000101001010010001001000000000"

    packet, rest = Packet.from_bin_str(bin_str)
    assert packet.version == 1
    assert packet.packet_id == 6
    assert len(packet.children) == 2
    assert packet.children[0].literal_value == 10
    assert packet.children[1].literal_value == 20
    assert rest == "0000000"

def test_part_0c() -> None:
    bin_str = hex2bin("EE00D40C823060")
    assert bin_str == "11101110000000001101010000001100100000100011000001100000"

    packet, rest = Packet.from_bin_str(bin_str)
    assert packet.version == 7
    assert packet.packet_id == 3
    assert len(packet.children) == 3
    assert packet.children[0].literal_value == 1
    assert packet.children[1].literal_value == 2
    assert packet.children[2].literal_value == 3
    assert rest == "00000"

@pytest.mark.parametrize(
    ("input_string", "output"),
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_part_1(input_string: str, output: int) -> None:
    binary = hex2bin(input_string)
    root, rest = Packet.from_bin_str(binary)
    assert root.sum_versions() == output


def test_part_2() -> None:
    os.chdir(os.path.dirname(__file__))
    with open("data/test_day_15.in") as input_file:
        pass
