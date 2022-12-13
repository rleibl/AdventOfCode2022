
f = open('input')
lines = f.readlines()

registerX = 1
registerTmp = 0
CPUbusy = False
tick = 0

SUM = 0

commands = iter(lines)

while True:

    tick += 1

    if tick % 20 == 0:
        if tick in (20, 60, 100, 140, 180, 220):
            SUM += tick * registerX
        print(f'{tick} {registerX} sum {SUM}')


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

print(SUM)
