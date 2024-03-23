import math


r = float(input("enter number\n"))
pi = math.pi
method = input("enter calculation method:[cincrumence(c),width]\n")
if method == "luas":
    L = r * r * pi
    print(L)
    print("ignore the 5th number and so on")
elif method == "keliling" or method == "cincrumence" or "c":
    K = 2 * pi * r
    print(K)
    print("ignore the 5th number and so on")
else:
    exit()
