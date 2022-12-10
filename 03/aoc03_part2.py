
f = open('input')
data = f.readlines()

sum_of_priorities = 0

for i in range(0, len(data)-1, 3):

    l1 = data[i  ][:-1]
    l2 = data[i+1][:-1]
    l3 = data[i+2][:-1]

    match = [ i for i in l1 if i in l2 and i in l3 ][0]

    val = 0
    if ord(match) < ord('a'):
        val = ord(match) - ord('A') + 27
    else:
        val = ord(match) - ord('a') + 1

    sum_of_priorities += val

print(sum_of_priorities)

