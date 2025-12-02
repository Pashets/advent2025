with open("task.txt") as f:
    ranges = [tuple(map(int, i.split('-'))) for i in f.read().split(',')]
print(ranges)
q = []
for r in ranges:
    for a in range(r[0], r[1]+1):
        str_a = str(a)
        len_str_a = len(str_a)
        left_part = str_a[:len_str_a//2]
        right_part = str_a[len_str_a//2:]
        print(left_part, right_part)
        if len_str_a %2 ==1 :
            continue
        if left_part == right_part:
            print(a)
            q.append(a)
print(sum(q))