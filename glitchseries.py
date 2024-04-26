import sys
x = []
for listen in range(int(sys.argv[1])):
    x.append(listen)
t = [1/2, 2/3, 3/4, 4/5]
c = [2/1, 3/2, 4/3, 5/4]
class series:
    def __init__():    
        for i in x:
            for u in t:
                v = lambda x: i+u*x
                print(list(map(v, c)), end="")
series.__init__()