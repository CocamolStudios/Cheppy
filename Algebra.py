import sympy as sy
import numpy as np
import math
from colorama import Fore
import time
import tqdm

class ALB1:
    def alb_1_a(self):
        while True:
            a = sy.symbols(input("var1:"))
            b = sy.symbols(input("var2:"))
            c = int(input("integer1:"))
            d = int(input("integer2:"))
            e = input("Operator:")
            a1 = a*c + b*d
            a2 = a*c - b*d
            a3 = a*c * b*d
            a4 = a*c / b*d
            a5 = a*c ** b*d
            f = [a1, a2, a3, a4, a5]
            if e == "+":
                print("functions:", f)
                print(a1)
            elif e == "-":
                print("functions:", f)
                print(a2)
            elif e == "*":
                print("functions:", f)
                print(a3)
            elif e == "/":
                print("functions:", f)
                print(a4)
            elif e == "^":
                print("functions:", f)
                print(a5)

    def alb_1_b(self):
        a = sy.symbols(input("var1:"))
        b = sy.symbols(input("var2:"))
        c = sy.symbols(input("var3:"))
        d = int(input("integer1:"))
        e = int(input("integer2:"))
        f = input("Operator:")
        a1 = (a*d + b*e) ** 2 + c
        a2 = (a*d + b*e) ** 2 - c
        a3 = (a*d + b*e) ** 2 * c
        a4 = (a*d + b*e) ** 2 / c
        a5 = (a*d + b*e) ** 2 ** c
        g = [a1, a2, a3, a4, a5]
        if f == "+":
            print("functions:", g)
            print(a1)
        elif f == "-":
            print("functions:", g)
            print(a2)
        elif f == "*":
            print("functions:", g)
            print(a3)
        elif f == "/":
            print("functions:", g)
            print(a4)
        elif f == "^":
            print("functions:", g)
            print(a5)

class EquationA:
    def eq_1(self):
        while True:
            a = sy.symbols(input("unknown:"))
            b = int(input("Unknown coefficient:"))
            c = int(input("known:"))
            d = a = c / b
            print(Fore.GREEN+"unknown:", int(d))
            print(Fore.RESET)

    def eq_2(self):
        while True:
            a = sy.symbols(input("unknown:"))
            b = int(input("Unknown coefficient:"))
            c = int(input("known:"))
            d = input("Operator:")
            e = int(input("integer:"))
            a1 = c + e
            a2 = c - e
            if d == "+":
                f = a = a2 / b
                print(Fore.GREEN+"unknown:", int(f))
                print(Fore.RESET)
            elif d == "-":
                f = a = a1 / b
                print(Fore.GREEN + "unknown:", int(f))
                print(Fore.RESET)

    def eq_3(self):
            a = sy.symbols(input("unknown1:"))
            b = sy.symbols(input("unknown2:"))
            c = int(input("known:"))
            d = input("Operator:")
            e = None
            a1 = (a + b)
            a2 = (a - b)
            if a == b:
                e = 2
                if d == '+':
                    print("Type:", a1)
                    x = a = c / e
                    print(Fore.GREEN+"unknown:", int(x))
                    print(Fore.RESET)
                elif d == '-':
                    e = int(input("Unknown coefficient:"))
                    a2 = (e*a - b)
                    print("Type:", a2)
                    x = a = c / e
                    print(Fore.GREEN + "unknown:", int(x))
                    print(Fore.RESET)
            else:
                print("in eq_4")

    def eq_4(self):
        while True:
            a = sy.symbols(input("unknown1:"))
            b = sy.symbols(input("unknown2:"))
            c = int(input("known:"))
            d = input("Operator:")
            e = None
            a1 = (a + b)
            a2 = (a - b)
            if not a == b:
                print("For", a)
                e = a
                if d == '-':
                    x = a = c - e
                    print("Type:", a2)
                    print(Fore.GREEN + "unknown:", x)
                    print(Fore.RESET)
                    time.sleep(1.23)
                    print("For", b)
                    e = b
                    x = a = c - e
                    print("Type:", a2)
                    print(Fore.GREEN + "unknown:", x)
                    print(Fore.RESET)
                    time.sleep(1.23)
                    e = a
                elif d == '+':
                    x = a = c + e
                    print("Type:", a1)
                    print(Fore.GREEN + "unknown:", x)
                    print(Fore.RESET)
                    time.sleep(1.23)
                    print("For", b)
                    e = b
                    x = a = c + e
                    print("Type:", a1)
                    print(Fore.GREEN + "unknown:", x)
                    print(Fore.RESET)
            else:
                print("in eq_3")

    def eq_5(self):
        while True:
            print("second degree equation______")
            a = int(input("Please Enter a: "))
            b = int(input("Please Enter b: "))
            c = int(input("Please Enter c: "))
            delta = b * b - 4 * a * c
            if delta == 0:
                x = (-b + math.sqrt(delta))
                print("Moadele Yek javab darad. X=", x)
            elif delta < 0:
                print("Moadele javabe haghighi nadarad!")
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                print("Moadele 2 javab darad.\n X1= ", x1, "\nX2= ", x2)

class EquationB:
    def eq_1(self):
        while True:
            x = int(input("Count of Unknown coefficient:"))
            li = []
            for i in range(x):
                x2 = int(input('NUM:'))
                li.append(x2)
            print(li)
            y = max(li)
            print(y)
            a = sy.symbols(input("unknown:"))
            b = int(input("Known:"))
            c = a = b / y
            print(Fore.GREEN + "unknown:", int(c))
            print(Fore.RESET)
            print("Unknown coefficient:", y)

    def eq_2(self):
        while True:
            x = int(input("Count:"))
            x2 = int(input("Count of Unknown coefficient:"))
            x3 = x * x2 - (x + 1)
            Memory = {}
            for i in range(x):
                y = str(input("Bit1:"))
                z = sy.symbols(input("unknown:"))
                Memory[y] = z
            Memory2 = {}
            for i in range(x2):
                y2 = str(input("Bit2:"))
                z2 = int(input("Unknown coefficient:"))
                Memory2[y2] = z2
            Memory3 = {}
            for i in range(x3):
                y3 = str(input("Bit3:"))
                z3 = {**Memory2, **Memory}
                Memory3[y3] = z3
            print("Left Side of Equal:", Memory3)
            Memory4 = {}
            for i in range(x - 1):
                y4 = str(input("Bit4:"))
                z4 = Memory3.keys()
                Memory4[y4] = z4
            Memory5 = []
            print("All:", Memory4)
            Memory5.append(Memory4.values())
            BC = {}
            for i in range(x2):
                y5 = str(input("KEYS:"))
                z5 = Memory5
                BC[y5] = z5
            BCO = {}
            x4 = x2 + 1
            print("Memory5:", Memory5)
            print("BC:", BC)
            print("BCO:", BCO)
            for i in range(x4):
                y6 = str(input("KEYS2:"))
                z6 = BC.values()
                BCO[y6] = z6
            Memory6 = {}
            for i in range(x2 * 2):
                y7 = str(input("KEYS3:"))
                z7 = BCO.items()
                Memory6[y7] = z7
            Memory7 = Memory6.values()
            print("Memory6:", Memory6)
            print("Memory7:", Memory7)
            print("BCO:", BCO)
            a1 = str(input("index of Unknown:"))
            b = int(input("Known:"))
            x1 = str(input("key of Unknown coefficient:"))
            b2 = Memory2.get(x1)
            c = Memory.get(a1)
            d = c = b / b2
            print(Fore.GREEN+"Equation:", Fore.WHITE+"d = c = b / b2")
            print(Fore.GREEN+"Unknown:", int(c))
            print("Unknown coefficient:", b2)
            print(Fore.RESET)
