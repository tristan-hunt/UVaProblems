import sys

#sys.stdin = open("input.txt")  #cheating since windows can't cat from command-line
                                # MAKE SURE TO REMOVE BEFORE SUBMITTING
# for (items, store, orders, order_amounts) in load():
prev = [-1]*99999          
prev[0] = 0
items = int(next(sys.stdin))   
store = next(sys.stdin).split()
store = [int(c) for c in store]
for i in range(0, items):   
    for j in range(0, len(prev) - store[i]):         # func(j,0,prev.size()-store[i])
        if (prev[j] != -1):
            index = j + store[i]
            if (prev[index] != -1 or prev[j] == items):
                prev[index] = items
            else:
                prev[index] = i
next(sys.stdin)
order_amounts = next(sys.stdin).split()
order_amounts = [int(o) for o in order_amounts]
for d in order_amounts:
    if (prev[d] == items):
        sys.stdout.write("Ambiguous\n")     #cout << "Ambiguous" << endl;            
    elif (prev[d] == -1):
        sys.stdout.write("Impossible\n")    #cout << "Impossible" << endl;
    else:
        res = list()            # vecstore res;
        while (d > 0):
            res.append(prev[d] + 1)
            d = d - store[prev[d]]
            
        res = res[::-1]                 #reverse(res.begin(), res.end());
        for j in range(0, len(res)):    #func(j,0,res.size())
            sys.stdout.write("{}".format(res[j]))#cout << res[j]
            if (j + 1 < len(res)):
                sys.stdout.write(" ")   
            else:
                sys.stdout.write("\n")