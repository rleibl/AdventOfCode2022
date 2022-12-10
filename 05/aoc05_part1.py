
import re

#                  [V]     [C]     [M]
#  [V]     [J]     [N]     [H]     [V]
#  [R] [F] [N]     [W]     [Z]     [N]
#  [H] [R] [D]     [Q] [M] [L]     [B]
#  [B] [C] [H] [V] [R] [C] [G]     [R]
#  [G] [G] [F] [S] [D] [H] [B] [R] [S]
#  [D] [N] [S] [D] [H] [G] [J] [J] [G]
#  [W] [J] [L] [J] [S] [P] [F] [S] [L]
#   1   2   3   4   5   6   7   8   9 

crates = [
        ['W', 'D', 'G', 'B', 'H', 'R', 'V'     ],
        ['J', 'N', 'G', 'C', 'R', 'F'          ],
        ['L', 'S', 'F', 'H', 'D', 'N', 'J'     ],
        ['J', 'D', 'S', 'V'                    ],
        ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
        ['P', 'G', 'H', 'C', 'M'               ],
        ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
        ['S', 'J', 'R'                         ],
        ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']
]

f = open('input')
data = f.readlines()

for l in data:

    if not l or l == '\n':
        break

    m = re.match('move (\d+) from (\d) to (\d)\n', l)

    mtimes = int(m.group(1))
    mfrom  = int(m.group(2)) - 1
    mto    = int(m.group(3)) - 1

    for t in range(mtimes):
        crates[mto].append( crates[mfrom].pop() )

result = ""
for pile in crates:
    result += pile.pop()

print(result)



