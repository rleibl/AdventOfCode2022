
import json

# # struct direntry
# 'a': {
#     'name': 'a',
#     'parent': ['/'],
#     'type': 'd',
#     'size': 0,
#     'entries': {}
# }

root = {
    '/': {
        'name': '/',
        'parent': '/',
        'type': 'd',
        'size': 0,
        'entries': {}
    }
}
cwd = root['/']
cpath = ['/']

dirnamesizes = {}
dirnamesizes2 = []

def setsize(directory):

    size = 0

    for file in directory['entries'].values():

        if file['type'] == 'd':
            size += setsize(file)
        else:
            size += int(file['size'])

    directory['size'] = size

    return size

def directory_sizes(directory):

    global dirnamesizes
    global dirnamesizes2

    dirnamesizes[directory["name"]] = directory["size"]
    dirnamesizes2.append((directory["name"], directory["size"]))
    print(f'{directory["name"]}: {directory["size"]}')

    for v in directory['entries'].values():

        if v['type'] == 'd':
            directory_sizes(v)
            

def cd(directory):

    global cwd
    global cpath
    global root

    if directory == "..":

        path = cwd['parent']
        cpath = cwd['parent']
        cwd = root['/']
        path = path[1:] # remove '/'
        for element in path:
            cwd = cwd['entries'][element]

        return

    if directory == "/":
        cwd = root['/']
        cpath = ['/']
        return

    if directory not in cwd['entries']:
        print(f"Directory has not been ls'd before: {directory}")
        e = {
            'name': directory,
            'parent': cpath.copy(),
            'type': 'd',
            'size': 0,
            'entries': {}
        }
        cwd['entries'][directory] = e
    
    cwd = cwd['entries'][directory]
    cpath.append(directory)

def ls(entry):

    global cwd
    global cpath

    (a, b) = entry.split(' ')

    e = {
        'name': b,
        'parent': cpath.copy(),
        'type': 'd',
        'size': 0,
        'entries': {}
    }

    if a == 'dir':
        e['name'] = b
    else:
        e['name'] = b
        e['type'] = 'f'
        e['size'] = a

    cwd['entries'][b] = e




f = open('input')
lines = f.readlines()

for l in lines:
    if not l or l == "\n":
        break


    #print("-------- current tree ------------")
    #print(json.dumps(root, indent=4))
    #print(root)
    print( " -- Current Path: ", cpath )

    l = l[:-1]

    if l[0] == "$":
        cmd = l[2:].split(" ")
        print(f'command: {cmd}')

        if cmd[0] == "cd":
            cd(cmd[1])
        elif cmd[0] == "ls":
            pass
        else:
            print("command not found: {cmd[0]}")
    else:
        ls(l)


setsize(root['/'])
print(json.dumps(root, indent=4))

directory_sizes(root['/'])

for k, v in dirnamesizes.items():
    print(f'{k} -> {v}')

dirnamesizes2.sort(key=lambda x: x[1])
for i in dirnamesizes2:
    print(f'{i[0]:10s} -> {i[1]}')

total_disk = 70_000_000
required   = 30_000_000
used       = 49_192_532

currently_free = total_disk - used
additional_required = required - currently_free
print("additionally required", additional_required)
for i in dirnamesizes2:
    if i[1] > additional_required:
        print(f'{i[0]:10s} -> {i[1]}')

