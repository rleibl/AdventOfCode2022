
import sys

f = open('input')
#f = open('example')
data = f.readlines()


def updateH():

    global nodes_visited

    # up or down
    uod = H[1] - T[1]

    # left or right
    lor = H[0] - T[0]

    # move, if the distance from Head to Tail is more than d.
    # Usually, d is 1, so Tail will catch up, but will not reach Head.
    # If we need to move diagonally, which is the case when Head is ahead
    # two in one direction and one in the other, we need to move 
    # in both directions, regardless.
    d = 1
    if (abs(lor) + abs(uod)) == 3: # we need to move diagonally
        #print("move diagonally")
        d = 0



    if lor > d:   # T is right of H
        T[0] += 1
    elif lor < - d: # T is left of H
        T[0] -= 1

    if uod > d:
        T[1] += 1
    elif uod < - d:
        T[1] -= 1

    nodes_visited.append((T[0], T[1]))
    nodes_visited = list(set(nodes_visited)) # make unique
    

    #print(f"H is at {H}")
    #print(f"T is at {T}")
    #print(f"Visited {nodes_visited}")
    #printMaze()

def printMaze():

    global run

    for y in range(100, -145, -1): # values entered after max/min values were calculated
        for x in range(-180, 3):
            if H[0] == x and H[1] == y:
                print('H', end='')
            elif T[0] == x and T[1] == y:
                print('T', end='')
            elif (x,y) in nodes_visited:
                print('#', end='')
            else:
                print('.', end='')

        print()
    print()

    if not run:
        i = input()
        if i.startswith('q'):
            sys.exit(0)
        elif i.startswith('r'):
            run = True
            
run = False
nodes_visited = []
T = [0,0]
H = [0,0]

for l in data:
    if not l or l == "\n":
        break

    l = l[:-1]

    (direction, steps) = l.split()
    steps = int(steps)

    match direction:
        case 'R':
            for s in range(steps):
                #print('right 1')
                H[0] += 1
                updateH()
        case 'L':
            for s in range(steps):
                #print('left 1')
                H[0] -= 1
                updateH()
        case 'U':
            for s in range(steps):
                #print('up 1')
                H[1] += 1
                updateH()
        case 'D':
            for s in range(steps):
                #print('down 1')
                H[1] -= 1
                updateH()

minx = min( [ e[0] for e in nodes_visited] )
maxx = max( [ e[0] for e in nodes_visited] )
print(f'x min: {minx}')
print(f'x max: {maxx}')

miny = min( [ e[1] for e in nodes_visited] )
maxy = max( [ e[1] for e in nodes_visited] )
print(f'y min: {miny}')
print(f'y max: {maxy}')


printMaze()
print(len(nodes_visited))
