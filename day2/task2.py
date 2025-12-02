with open("task.txt") as f:
    ranges = [tuple(map(int, i.split('-'))) for i in f.read().split(',')]

# print(ranges)
q = []
for r in ranges:
    for a in range(r[0], r[1]+1):
        str_a = str(a)
        len_str_a = len(str_a)
        parts = []
        for i in range(1, len_str_a):
            if len_str_a % i == 0:
                small_parts=[]
                for j in range(0,len_str_a, i):
                    small_parts.append(str_a[j:j+i])
                parts.append(small_parts)
        # print(parts)
        for p in parts:
            if all(w==p[0] for w in p):
                # print(a)
                q.append(a)
                break

print(sum(q))