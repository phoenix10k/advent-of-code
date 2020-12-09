from typing import List, Dict

passports: List[Dict[str, str]] = []

with open('input.txt') as file:
    passport = {}
    for line in file:
        if line.strip():
            passport.update({part.split(':')[0]:part.split(':')[1] for part in line.split()})
        else:
            passports.append(passport.copy())
            passport = {}        
    passports.append(passport)

req = ['byr','iyr','eyr','hgt','hcl','ecl','pid']#,'cid']

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

count = 0
for passport in passports:
    print(passport)
    try:
        if not(1920 <= int(passport['byr']) <= 2002):
            print('bad byr')
            continue
        if not(2010 <= int(passport['iyr']) <= 2020):
            print('bad iyr')
            continue
        if not(2020 <= int(passport['eyr']) <= 2030):
            print('bad eyr')
            continue
        hgt = passport['hgt']
        if hgt.endswith('cm'):
            if not(150 <= int(hgt[:-2]) <= 193):
                print('bad hgt cm', int(hgt[:-2]))
                continue
        elif hgt.endswith('in'):
            if not(59 <= int(hgt[:-2]) <= 76):
                print('bad hgt in')
                continue
        else:
            print('bad hgt')
            continue
        
        hcl = passport['hcl']
        if len(hcl) != 7:
            print('bad hcl 1')
            continue
        if hcl[0] != '#':
            print('bad hcl 2')
            continue
        if not all(c in "0123456789abcdef" for c in hcl[1:]):
            print('bad hcl 3')
            continue
        if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            print('bad ecl')
            continue
        if len(passport['pid']) != 9:
            print('bad pid')
            continue
        pid = int(passport['pid'])
        count += 1
    except Exception as e:
        print(e)

print(count)
