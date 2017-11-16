#!/usr/bin/env python3
try:
    import sys
    for s in sys.argv:
        s = int(sys.argv[1])-3500
        if s <= 0 :
            s = 0
        elif s > 0 and s <= 1500:
            s = s * 0.03
        elif s > 1500 and s <= 4500:
            s = s * 0.1 -105
        elif s > 4500 and s <= 9000:
            s = s * 0.2 -555
        elif s > 9000 and s <= 35000:
            s = s * 0.25 -1005
        elif s > 35000 and s <= 55000:
            s = s * 0.3 -2755
        elif s > 55000 and s <= 80000:
            s = s * 0.35 -5505
        elif s > 80000:
            s = s * 0.45 -13505
    print(format(s,".2f"))
except:
    print("Parameter Error")
