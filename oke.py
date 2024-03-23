import keyboard
import os
from colorama import Style, Fore
import math

print("pilih diantara:")
print("[konversi, penilaian, santoon tv, berat, data]")
select = input("")


def konversi():
    detik = float(input("detik: "))
    print(detik * 1000, "ms")
    print(detik, "s")
    print(detik / 60, "m")
    print(detik / 3600, "h")
    print(detik / 86400, "d")


def nilai():
    print("b.inggris")
    eng = int(input("masukkan nilai:"))
    print("b.indo")
    id = int(input("masukkan nilai:"))
    print("mtk")
    math = int(input("masukkan nilai:"))
    print("ipa")
    scince = int(input("masukkan nilai:"))
    print("ips")
    social = int(input("masukkan nilai:"))
    total = eng + id + math + scince + social
    percent = float(total / 100)
    print(f"total={total}")
    print(f"{percent}%")
    if percent <= 3.15:
        print("gagal")
    else:
        print("lulus")


def cho_cho_madafxxka():
    print(f"{Fore.YELLOW}santoon tv{Style.RESET_ALL}")
    isi = input("masukkan apa saja ")
    if isi == "kereta api":
        os.system(
            "start https://www.youtube.com/watch?v=1ms-ZyZZK4U&ab_channel=SANTOONTV"
        )
    elif isi == "laut":
        os.system(
            "start https://www.youtube.com/watch?v=wEuJg2S6ja8&ab_channel=SANTOONTV"
        )


def berat():
    b1 = 4096
    b2 = b1 / 2
    b3 = b2 / 2
    b4 = b3 / 2
    b5 = b4 / 2
    b6 = b5 / 2

    c = b1 + b2 + b3 + b4 + (b5 * 2) + b6

    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)
    print(b6)

    print(c)

    h = c - 3947.197 - 2400
    print(h)


def data():
    print("pilih diantara: [b,kb,mb,gb,tb,pb,e]")
    isi = input("")
    if isi == "b":
        b = float(input("masukkan byte "))
        kb = b / 1000
        mb = b / 1e-6
        gb = b / 1e-9
        print(b, "byte")
        print(kb, "kilobyte")
        print(mb, "megabyte")
        print(gb, "gigabyte")
        print("mohon maaf, disini tidak tersedia tb karena ngitungnya agak susah")
        print("mohon maaf, disini tidak tersedia pb karena ngitungnya terlalu susah")
    elif isi == "kb":
        kb = float(input("masukkan kb "))
        b = kb * 8000
        mb = kb / 1000
        gb = kb / 1e6
        tb = kb / 1e9
        print(b, "byte")
        print(kb, "kilobyte")
        print(mb, "megabyte")
        print(gb, "gigabyte")
        print(tb, "terabyte")
        print("mohon maaf, disini tidak tersedia pb karena ngitungnya terlalu susah")
    elif isi == "mb":
        mb = float(input("masukkan mb "))
        b = mb * 1e6
        kb = mb * 1000
        gb = mb / 1000
        tb = mb / 1e6
        pb = mb / 1e9
        print(b, "byte")
        print(kb, "kilobyte")
        print(mb, "megabyte")
        print(gb, "gigabyte")
        print(tb, "terabyte")
        print(pb, "petabyte")
    elif isi == "gb":
        gb = float(input("masukkan gb "))
        b = gb * 1e9
        kb = gb * 1e6
        mb = gb * 1000
        tb = gb / 1000
        pb = gb / 1e6
        print(b, "byte")
        print(kb, "kilobyte")
        print(mb, "megabyte")
        print(gb, "gigabyte")
        print(tb, "terabyte")
        print(pb, "petabyte")
    elif isi == "tb":
        tb = float(input("masukkan tb "))
        b = tb * 1e12
        kb = tb * 1e9
        mb = tb * 1e6
        gb = tb * 1000
        pb = tb / 1000
        print(b, "byte")
        print(kb, "kilobyte")
        print(mb, "megabyte")
        print(gb, "gigabyte")
        print(tb, "terabyte")
        print(pb, "petabyte")
    elif isi == "pb":
        pb = float(input("masukkan pb "))
        b = pb * 1e15
        kb = pb * 1e12
        mb = pb * 1e9
        gb = pb * 1e6
        tb = pb * 1000
        print(b, "byte")
        print(kb, "kilobyte")
        print(mb, "megabyte")
        print(gb, "gigabyte")
        print(tb, "terabyte")
        print(pb, "petabyte")
    elif isi == "e" or isi == "E":
        e = math.e
        print(e)


if select == "konversi":
    konversi()
elif select == "nilai" or select == "penilaian":
    nilai()
elif select == "berat":
    berat()
elif select == "data":
    data()
else:
    print(f"{Fore.RED}tidak diketahui!{Style.RESET_ALL}")
