
forest = []

f = open('input')
#f = open('example')
for l in f.readlines():
    if not l or l == "\n":
        break
    l = l[:-1]

    row = []
    for e in l:
        row.append(int(e))

    forest.append(row)

length = len(forest)
count = 2 * length + 2 * (length-2) # borders are visible

for x in range(1, length-1):
    for y in range(1, length-1):

        height = int(forest[y][x]) # note that x and y are flipped in forest
        print(f'Looking at [{x},{y}]. Height is {height} ')

        # from the top 
        for i in range(0, y):
            if forest[i][x] >= height:
                break
        else:
            count += 1
            continue

        # from the bottom
        for i in range(length-1, y, -1):
            if forest[i][x] >= height:
                break
        else:
            count += 1
            continue

        # from the left
        for i in range(0, x):
            if forest[y][i] >= height:
                break
        else:
            count += 1
            continue

        # from the right
        for i in range(length-1, x, -1):
            if forest[y][i] >= height:
                break
        else:
            count += 1
            continue

print(count)
