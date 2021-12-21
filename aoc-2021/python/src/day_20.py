import os
from typing import TextIO


def parse_input(input_file: TextIO) -> tuple[list[str], str]:
    program = next(input_file).strip()
    next(input_file)
    image = [".." + line.strip() + ".." for line in input_file]
    image.insert(0, "." * len(image[0]))
    image.insert(0, "." * len(image[0]))
    image.append("." * len(image[0]))
    image.append("." * len(image[0]))
    print_image(image)
    return image, program


def print_image(image: list[str]) -> None:
    for line in image:
        print(line)


def enhance(image: list[str], program: str) -> list[str]:
    pc = program[0] if image[0][0] == "." else program[-1]  # padding char
    new_image = [pc * (len(image[0]) + 2)]
    new_image.append(pc * (len(image[0]) + 2))
    for i in range(1, len(image) - 1):
        new_line = pc * 2
        for j in range(1, len(image[0]) - 1):
            bits = (
                image[i - 1][j - 1 : j + 2]
                + image[i][j - 1 : j + 2]
                + image[i + 1][j - 1 : j + 2]
            )
            bits = bits.replace(".", "0")
            bits = bits.replace("#", "1")
            idx = int(bits, base=2)
            new_line += program[idx]
        new_line += pc * 2
        new_image.append(new_line)

    new_image.append(pc * (len(image[0]) + 2))
    new_image.append(pc * (len(image[0]) + 2))
    print_image(new_image)
    return new_image


def count_pixels(image: list[str]) -> int:
    return sum(line.count("#") for line in image)


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    with open("../data/day_20.in") as input_file:
        image, program = parse_input(input_file)

    image = enhance(image, program)
    image = enhance(image, program)

    print("part 1:", count_pixels(image))
    
    for _ in range(48):
        image = enhance(image, program)

    print("part 2:", count_pixels(image))
