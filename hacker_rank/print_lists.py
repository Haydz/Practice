T = int(raw_input().strip())

L = []


for x in range(T):
    args = raw_input().strip().split(" ")
    if args[0] == 'insert':
        L.insert(int(args[1]),int(args[2]))
    elif args[0] == 'remove':
        L.remove(int(args[1]))
    elif args[0] == 'append':
        L.append(int(args[1]))
    elif args[0] == 'sort':
        L.sort()
    elif args[0] == 'pop':
        L.pop(-1)
    elif args[0] == 'reverse':
        L.reverse()
    elif args[0] == 'print':
        print L




B = [0,2]
c = B.pop(-1)
print c

D = [1,2,3,4,123,546,3,3,'abc']
D.remove(3)
D.append(5)
print D

