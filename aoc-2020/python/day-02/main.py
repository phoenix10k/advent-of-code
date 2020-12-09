import parse

count = 0
with open('input.txt') as file:
    for line in file:
        r = parse.parse("{min:d}-{max:d} {char}: {pass}", line)
        print(r)
        #if r['min'] <= r['pass'].count(r['char']) <= r['max']:
        if (r['pass'][r['min']-1] == r['char']) != (r['pass'][r['max']-1] == r['char']):
            count +=1
print(f"count: {count}")
