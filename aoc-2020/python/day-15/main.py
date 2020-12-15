
def get_2020th_num(input_list):
    last_seen = {k:i for i, k in enumerate(input_list[:-1])}
    next_num = input_list[-1]
    for i in range(len(input_list) - 1, 2019):
        when = last_seen.get(next_num)
        last_seen[next_num] = i
        if when is None:
            next_num = 0
        else:
            next_num = i - when
    return next_num

for input_list in[[0,3,6],[1,3,2],[2,1,3],[1,2,3],[2,3,1],[3,2,1],[3,1,2],[11,18,0,20,1,7,16]]:
    print(get_2020th_num(input_list))