import itertools

mask_on = 0
mask_off = 0
floating_bits = set()
mem = {}

with open('input.txt') as file:
    for line in file:
        lhs, rhs = line.split(' = ')
        if lhs == 'mask':
            floating_bits = set()
            mask_off = (1<<37) - 1
            mask_on = 0
            for i, x in enumerate(reversed(rhs.strip())):
                if x == '0':
                    pass
                elif x == '1':
                    mask_on |= 1 << i
                elif x == 'X':
                    floating_bits.add(i)
                    mask_off ^= 1 << i
                else:
                    raise RuntimeError("Bad mask.")
            print(f'mask_on {mask_on:>036b}')
            print(f'mask_off {mask_off:>036b}')
            print('floating_bits', ''.join('1' if f in floating_bits else '0' for f in range(36, -1, -1)))
        elif lhs[:3] == 'mem':
            idx = int(lhs[4:-1])
            idx |= mask_on
            idx &= mask_off
            addresses = [idx]
            for f in sorted(floating_bits):
                addresses += [a | (1 << f) for a in addresses]

            # ans = (int(rhs) & mask_off) | mask_on
            for idx in addresses:
                mem[idx] = int(rhs)
                print('mem[', idx, '] =', rhs)
        else:
            raise RuntimeError("Unknown instruction.")

print('sum:', sum(mem.values()))
