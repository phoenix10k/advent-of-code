import itertools

mask_on = 0
mask_off = 0
mem = {}

with open('input.txt') as file:
    for line in file:
        lhs, rhs = line.split(' = ')
        if lhs == 'mask':
            mask_off = (1<<37) - 1
            mask_on = 0
            for i, x in enumerate(reversed(rhs.strip())):
                if x == '0':
                    mask_off ^= 1 << i
                elif x == '1':
                    mask_on |= 1 << i
                elif x != 'X':
                    raise RuntimeError("Bad mask.")
            print(f'mask_on {mask_on:>036b}')
            print(f'mask_off {mask_off:>036b}')
        elif lhs[:3] == 'mem':
            idx = int(lhs[4:-1])
            ans = (int(rhs) & mask_off) | mask_on
            mem[idx] = ans
            print('mem[', idx, '] =', ans)
        else:
            raise RuntimeError("Unknown instruction.")

print('sum:', sum(mem.values()))
