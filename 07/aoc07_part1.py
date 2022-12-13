
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

def setsize(directory):

    size = 0

    for name in directory['entries'].keys():

        file = directory['entries'][name]

        if file['type'] == 'd':
            s = setsize(file)
            file['size'] = int(s)
            size += int(s)
        else:
            size += int(file['size'])

    return size

def sumlarger(directory):

    size = 0
    for v in directory['entries'].values():

        if v['type'] == 'd':
            #print(f'{v["name"}: v["size"]')
            if v['size'] < 100000:
                print(f'{v["name"]}: {v["size"]}')
                size += v['size']

            size += sumlarger(v)

    return size
            

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

total = sumlarger(root['/'])
print(total)
