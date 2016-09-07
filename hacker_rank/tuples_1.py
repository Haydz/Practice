T = int(raw_input().strip())
# THE ISSUE WAS THAT I HAD TO CONVERT STRING TO INTEGER TO HASH CORRECTLY
L = []
TUPLE = ()
TUPLE2= ()
#for x in range(T):
args = raw_input().strip().split(" ")
for x in range(T):
    args[x] = int(args[x])
test = tuple(args)
#print type(test)
TUPLE = hash(TUPLE + test)
#TUPLE2 = TUPLE2 + test
print TUPLE
#print TUPLE2