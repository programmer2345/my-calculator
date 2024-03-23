import math

# epep
# balok
v1 = int(input("enter length "))
v2 = int(input("enter width "))
v3 = int(input("enter height "))
x = v1
y = v3
z = v2
# volume balok
Vbalok = x * y * z
print(f"the volume of block is: {Vbalok}")
# lp balok
lpbalok = 2 * x * z + x * y + z * y
print(f"the surface area of block is: {lpbalok}")
# me-leng-kung
print("makin rumit nih")
# bola
print("ball")
r = float(input("enter radius"))
pi = math.pi
type_1 = input("half ball or full of ball? ")
if type_1 == "half" or "setengah":
    Vsetengah = 2 / 3 * pi * r
    print(f"the volume of half a ball is: {Vsetengah}")

elif type_1 == "full":
    V = 4 / 3 * pi * r * r * r
    print(f"the volume of full ball is: {V}")

# lp bola
lp = 4 * pi * r * r
print(f"the survace area of ball is: {lp}")

# kerucut
