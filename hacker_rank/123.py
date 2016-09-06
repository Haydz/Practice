N = 3
n1 = []
def printing(N):
    for x in range(0, (N+1)):
       n1.append(x)
    print N

printing(N)
print n1
b = ''.join(n1)
print b
for x in ''.join(n1):
    print x,