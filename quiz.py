import random
from colorama import Fore, Style
import time


a = random.randint(1, 100)
b = random.randint(1, 100)
adistm = random.randint(1, 10)
bdistm = random.randint(1, 10)
x = input("pilih operator: [+, -, *, /]")
if x == "+":
    c1 = a + b
    answer1 = int(input(f"berapakah hasil dari: {a}{x}{b}? "))
    if answer1 != c1:
        print(f"{Fore.RED}salah!{Style.RESET_ALL}")
        print("jawaban yang benar adalah:", c1)
    else:
        print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
        print("jawabannya adalah:", c1)
elif x == "-":
    c2 = a - b
    answer2 = int(input(f"berapakah hasil dari: {a}{x}{b}? "))
    if answer2 != c2:
        print(f"{Fore.RED}salah!{Style.RESET_ALL}")
        print("jawaban yang benar adalah:", c2)
    else:
        print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
        print("jawabannya adalah:", c2)
elif x == "*":
    print("=" * 30)
    print("   PILIH TINGKAT KESULITAN")
    print("=" * 30)
    print(f"{Fore.GREEN}mudah:                     [1]{Style.RESET_ALL}")
    print(f"{Fore.RED}sulit:                     [2]{Style.RESET_ALL}")
    print("=" * 30)
    sltm = input("")
    if sltm == "1":
        c31 = adistm * bdistm
        ans31 = int(input(f"berapakah hasil dari: {adistm}{x}{bdistm}"))
        if ans31 != c31:
            print(f"{Fore.RED}salah!{Style.RESET_ALL}")
            print("jawaban yang benar adalah:", c31)
        else:
            print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
            print("jawabannya adalah:", c31)
    elif sltm == "2":
        c32 = a * b
        ans32 = int(input(f"berapakah hasil dari: {a}{x}{b}"))
        if ans32 != c32:
            print(f"{Fore.RED}salah!{Style.RESET_ALL}")
            print("jawaban yang benar adalah:", c32)
        else:
            print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
            print("jawabannya adalah:", c32)
elif x == "/":
    print("=" * 30)
    print("   PILIH TINGKAT KESULITAN")
    print("=" * 30)
    print(f"{Fore.GREEN}mudah:                     [1]{Style.RESET_ALL}")
    print(f"{Fore.RED}sulit:                     [2]{Style.RESET_ALL}")
    print("=" * 30)
    slds = input("")
    if slds == "1":
        c41 = adistm / bdistm
        rc41 = round(c41)
        answer41 = float(input(f"brapakah hasil dari: {adistm}{x}{bdistm}? "))
        if answer41 != c41:
            print(f"{Fore.RED}salah!{Style.RESET_ALL}")
            print("jawaban yang benar adalah:", c41)
            print("jika:")
            print("jawabannya mendekati maka:")
            if answer41 == rc41:
                print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}salah!{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
            print("jawabannya adalah:", c41)
            print("jika:")
            print("jawabannya mendekati maka:")
            if answer41 == rc41:
                print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}salah!{Style.RESET_ALL}")
    elif slds == "2":
        c42 = a / b
        answer42 = float(input(f"berapakah hasil dari: {a}{x}{b}? "))
        if answer42 != c42:
            print(f"{Fore.RED}salah!{Style.RESET_ALL}")
            print("jawaban yang benar adalah:", c42)
        else:
            print(f"{Fore.GREEN}benar!{Style.RESET_ALL}")
            print("jawabannya adalah:", c42)
else:
    print(f"{Fore.RED}operator tidak diketahui!{Style.RESET_ALL}")
    exit()
