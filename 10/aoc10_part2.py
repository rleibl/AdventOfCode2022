
f = open('input')
lines = f.readlines()

registerX = 1
registerTmp = 0
CPUbusy = False
tick = 0

SUM = 0

commands = iter(lines)

while True:

    t = tick % 40

    if t == 0:
        print()

    if registerX in (t-1, t, t+1):
        print('#', end='')
    else:
        print('.', end='')

    tick += 1

    if CPUbusy:
        registerX += registerTmp # value is increased after two cycles
        CPUbusy = False
        continue

    cmd = next(commands)
    if not cmd or cmd == "\n":
        break

    if cmd == 'noop\n':
        continue

    (op, val) = cmd.split()
    val = int(val)

    registerTmp = val
    CPUbusy = True
