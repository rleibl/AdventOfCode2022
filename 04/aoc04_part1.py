
import re

f = open('input')
data = f.readlines()

s = 0

for l in data:

    if not l or l == '\n':
        break

    r = re.match('(\d+)-(\d+),(\d+)-(\d+)\n', l)
    (l1, l2, r1, r2) = r.group(1, 2, 3, 4)
    (l1, l2, r1, r2) = (int(l1), int(l2), int(r1), int(r2))

    # left contained in right
    if l1 >= r1 and l2 <= r2:
        s += 1

    # right contained in left
    elif r1 >= l1 and r2 <= l2:
        s += 1

print(s)
