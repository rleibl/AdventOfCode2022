
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

    # left is completely left of right
    if l1 < r1 and l2 < r1:
        pass
    # left is completely right of right
    elif l1 > r2 and l2 > r2:
        pass
    else:
        s += 1

print(s)
