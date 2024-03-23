matematika = input("pilih umum atau tidak umum? ")
if matematika == "umum":
    x = int(input("masukkan angka bertama: "))
    y = int(input("masukkan angka kedua: "))
    print("masukkan operator:[+, -, x, /]")
    op = input("")
    if op == "+":
        z = x + y
        print(z)
    elif op == "-":
        z = x - y
        print(z)
    elif op == "x":
        z = x * y
        print(z)
    elif op == "/":
        z = x / y
        print(z)
elif matematika == "tidak umum":
    x = float(input("masukkan angka"))
    persentase = int(input("masukkan persentase "))
    hasil = x / persentase
    print(hasil)
