max_seat = 0
seats = set()
with open('input.txt') as file:
    for input in file:
        row = 0
        col = 0
        for idx, char in enumerate(input[:7]):
            if char == 'B':
                row += pow(2, 6-idx)
        for idx, char in enumerate(input[7:]):
            if char == 'R':
                col += pow(2, 2-idx)

        seat = row * 8 + col
        print('seat:', seat)

        max_seat = max(max_seat, seat)
        seats.add(seat)

print('max_seat:', max_seat)

print('missing:', set(range(max_seat)) - seats)
