import numpy

import time

import tqdm

import math

import scipy

import matplotlib.pyplot as plt

import sympy

import fractions

import colorama

import pylj

def small_large_and_equal_operators(x, y):
    if x > y:
        print(x, ' is larger than', y)

    elif x < y:
        print(y, ' is larger than', x)

    elif x == y:
        print(x, ' is equal with', y)

def bump(x):
        a = x + 1
        print(a)
        print(a + 1)
        print(a + a + 1)
        print(a + a + a + 1)
        print(a + a + a + a + 1)
        print(a + a + a + a + a + 1)
        print(a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)

# Fibonacci Series using Dynamic Programming
def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    FibArray = [0, 1]

    while len(FibArray) < n + 1:
        FibArray.append(0)

    if n <= 1:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = fibonacci(n - 1)

        if FibArray[n - 2] == 0:
            FibArray[n - 2] = fibonacci(n - 2)

    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]
    print(fibonacci(23))

def maxi():
    x = int(input("number of numbers:"))
    z = []
    for i in range(x):
        y = int(input('NUM:'))
        z.append(y)
    print(max(z))

def Count(n):
    print(n)
    Count(n+1)
    # Don't call this function (Count)

def factorial(n):
    if n == 0 or n == 1:
        F = 1
    else:
        F = 1
        for i in range(1, n + 1):
            F *= i
    print(F)

def Alpha_0_statement(n):
    x = 4*n - 1
    print(x, 'The first phase in Crowley''s group')
    y = x * (3*n + 1)
    print(y, 'The second phase of Crowley''s collection')
    z = y * (5*n / 1)
    print(z, 'The last phase of Crowley''s collection')
    print('This function is Crowley''s alpha-0 sum statement, which shows the phases one by one.')

def Binomial_analogy(n):
    x = n * n - n + n * (n * n - n + n) ^ (n * n - n + n)
    print(x)
    if n < x:
        print('True, ', x,'is greater than', n)
    elif n > x:
        print('False ', n,'is greater than', x)
    elif n == x:
        print('Equal ', n,'is Equal with',x)

def Unequal_argument(n):
    x = n + n
    y = x - n
    if y == n:
        print(True)
    else:
        print(False)

def Zayg_rule(n):
    x = n + n
    y = -n
    z = x = y
    print(x, y, z, z, '"E"' == True)

def math_lite():
    while True:
     x = int(input('ORACLE >'))
     y = int(input('ORACLE >'))
     z = input('OPERATOR >')
     if z == '+':
        print(x + y)
     elif z == '-':
        print(x - y, '1 mode')
        print(y - x, '2 mode')
     elif z == '*':
        print(x * y)
     elif z == '**':
        print(x ** y, '1 mode')
        print(y ** x, '2 mode')
     elif z == '/':
        print(x / y, '1 mode')
        print(y / x, '2 mode')
     elif z == '%':
        print(x % y, '1 mode')
        print(y % x, '2 mode')
     else:
         print(colorama.Fore.RED,'[Error]', colorama.Fore.RESET,colorama.Fore.WHITE,'<Unspecified entry>')

def Alpha_1(α, β):
    y = fractions.Fraction(α, α ^ 2)
    if β == y:
        print(y, '= β')
        print(β, 'Beta is Equal to alpha over alpha to the power of two')
    elif not β == y:
        print(y, '= β')
        print(β, 'Beta is Not Equal to alpha over alpha to the power of two.')
    print('\n',y == β)
    print('\nAlpha-1')

def Wrights_Theorem(α, β, Δ, θ):
     x = math.radians(α)
     y = math.sin(x)
     x2 = math.radians(β)
     y2 = math.sin(x2)
     x3 = math.radians(Δ)
     y3 = math.sin(x3)
     x4 = math.radians(θ)
     y4 = math.sin(x4)
     z = y - y2
     z2 = y2 - y3
     z3 = y3 - y4
     z4 = z * z2 - y
     z5 = z2 * z3 - y2
     z6 = z3 * z4 - y3
     z7 = z4 * z5 - y4
     Z = (z7 * z6 * z5 * z4) * (z7 * θ) * (z7 * θ)
     Z2 = Z - z7 - z6 - z5 - z4
     Z3 = Z2 * Z
     Z4 = Z3 * Z2
     Z5 = Z4 * Z3
     Z6 = Z5 * Z4 * Z3 * Z2 * Z - α - β - Δ - θ
     Z7 = Z6 * 2
     Z8 = Z7 * Z7 * Z7
     print(Z8)
     print('\n', α, β, Δ, θ, 'Up')
     x = math.radians(-α)
     y = math.sin(x)
     x2 = math.radians(-β)
     y2 = math.sin(x2)
     x3 = math.radians(-Δ)
     y3 = math.sin(x3)
     x4 = math.radians(-θ)
     y4 = math.sin(x4)
     z = -y - -y2
     z2 = -y2 - -y3
     z3 = -y3 - -y4
     z4 = -z * -z2 - -y
     z5 = -z2 * -z3 - -y2
     z6 = -z3 * -z4 - -y3
     z7 = -z4 * -z5 - -y4
     Z = (-z7 * -z6 * -z5 * -z4) * (-z7 * -θ) * (-z7 * -θ)
     Z2 = -Z - z7 - z6 - z5 - -z4
     Z3 = -Z2 * -Z
     Z4 = -Z3 * -Z2
     Z5 = -Z4 * -Z3
     Z6 = -Z5 * -Z4 * -Z3 * -Z2 * -Z - -α - -β - -Δ - -θ
     Z7 = -Z6 * 2
     Z8 = -Z7 * -Z7 * -Z7
     print('\n', Z8)
     print('\n', -α, -β, -Δ, -θ, 'Up')

def polyarea(n, a):
    area = (4 * math.pow(20, 2)) / (4 * math.tan(math.pi / 4))
    print(area)

def second_degree_equation(a, b, c):
    print('Solve the quadratic equation ax**2 + bx + c = 0')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        sol1 = (-b - math.sqrt(d)) / (2 * a)
        sol2 = (-b + math.sqrt(d)) / (2 * a)
        print('The solution are {0} and {1}'.format(sol1, sol2))
    elif d == 0:
        sol1 = -b // (2 * a)
        print('The solution is {0} '.format(sol1))
    else:
        print('The equation has no answer')

def Pythagorean_numbers(a, b, c):
    a = int(input("please Enter Number1: "))
    b = int(input("please Enter Number2: "))
    c = int(input("please Enter Number3: "))
    if a * a == b * b + c * c or b * b == c * c + a * a or c * c == a * a + b * b:
        print("Yes")
    else:
        print("No")

def Prime_number(n):
    n = int(input('please input your n: '))
    accumulator = 0
    for i in range(1, n + 1):
        if n % i == 0:
            accumulator += 1
    if accumulator == 2:
        print('your number is prime')
    else:
        print('your number is not prime')

def The_theorem_of_the_two_zeta_formula(ζ):
    ζ = sympy.zeta(ζ ^ ζ)
    β = ζ + ζ
    y = sympy.sqrt(ζ + math.pi ** ζ + β ** ζ ** ζ)
    sympy.pprint(expr=y, use_unicode=True)

def g_beta_alpha(ε):
    Δ = sympy.sqrt(ε + ε ^ ε)
    λ = sympy.divisor_sigma(ε,  ε ^ 2)
    φ = sympy.factorial(ε)
    β = sympy.sqrt(φ)
    α = sympy.sqrt(β)
    Σ = α * β / φ
    g = λ + φ + sympy.sqrt(Σ) - Δ
    sympy.pprint(g)

def obvious_infinite(δ):
    a = sympy.sqrt(δ)
    x = sympy.symbols('η')
    y = a * a
    z = sympy.symbols('π')
    λ = sympy.sin(a) / y
    τ = sympy.log(λ)
    b = sympy.sqrt(τ - sympy.sqrt(λ) * x + y / z + sympy.sqrt(δ))
    sympy.pprint(b)

def The_transformation_of_Zayg(ρ):
    Σ = sympy.rad(ρ)
    μ = Σ * sympy.sqrt(ρ)
    x = sympy.symbols('λ')
    y = sympy.symbols('π')
    z = sympy.symbols('Ω')
    β = sympy.sin(μ) / x * y
    sympy.pprint(β)
    print('β =', z)

def collectivization(x):
    y = sympy.symbols('ζ')
    z = sympy.symbols('Δ')
    a = x * sympy.simplify(x + 3 + y) / z
    sympy.pprint(a)
    sympy.pprint(a + 1)
    sympy.pprint(a + a + 1)
    sympy.pprint(a + a + a + 1)
    sympy.pprint(a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)

def Sulfurosis(Σ):
    b = sympy.symbols('η')
    b2 = sympy.symbols('β')
    a = sympy.digamma(Σ) / b
    c = a - sympy.sqrt(Σ) / b2
    λ = c * Σ
    sympy.pprint(λ)

def Masdelos(x):
    φ = x * x ^ x
    β = sympy.symbols('β')
    λ = sympy.symbols('Σ')
    y = sympy.symbols('λ')
    μ = (x * φ / β - φ / λ) / y
    sympy.pprint(μ)

def Power_of_Zayg(x):
    a1 = sympy.symbols('η')
    a2 = sympy.symbols('ε')
    a3 = sympy.symbols('λ')
    a = a3 - x * x * x / a1
    b = a / a2 ** 2
    sympy.pprint(b)

def Product_table(x, y):
    for i in range(1, x):
        for j in range(1, y):
            print("{:3d}".format(i * j), end=" ")
        print()
    # According to x, it is better not to make y bigger than 1 to n

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    print(sum == n)

def binomial(x, y, n, m, s):
    a = (x + y) ^ n
    while n < m:
        for i in range(s):
            n += 1
            print("{:3d}".format(x + y ^ n), end="  ")
        print()

def herman_law(n, n2, x):
    h = ((n * n) ^ (n * n) ^ n)
    β = n ^ h
    α = β ^ (β * β) ^ h
    y = α * α
    while n < n2:
       for i in range(x):
           n += 1
           print("{:3d}".format(((n * n) ^ (n * n) ^ n)), end="  ")
       print()
    # Correct calculation up to five zero digits (x)
    # Correct calculation up to five zero digits (n2)

def herman_logarithmic_expansion(x, x2, x3):
    while x < x2:
       for i in range(x3):
           x += 1
           print("{:3d}".format(x * x ^ (x * x) ^ x * x), end="  ")
       print()

class HermanCirclePrinciples:
    def principle1(x):
        a = float(input("your number  :"))
        c = a + a
        Δ = c * math.pi
        α = x * x ^ x
        β = α * α
        λ = sympy.symbols('λ')
        d = α * β * Δ - sympy.sqrt(math.pi) / λ
        sympy.pprint(d)

    def principle2(x, y):
        a = float(input("your number  :"))
        c = a + a
        b = c * math.pi
        d = b * x ** y / a
        print(d)

    def principle3(x, y, z):
        a = float(input("your number  :"))
        c = a + a
        b = c * math.pi
        d = b / sympy.sqrt(z) ** y
        sympy.pprint(d)

def three_addition(x, c, z, x2):
    while x < c:
        y = x + 3
        for i in range(z):
                x += 3
                print("{:3d}".format(x + 0), end="  ")
        print()
    x3 = int(input())
    if x3 == x2:
        print("\n", c, " > ", x3)
# input is equal to x2
# x2 is equal to x


def Check_whether_f_is_convergent_or_not(x, y, z):
    t = time.time()
    dt = x / t
    f = t + dt
    b = f ** math.e
    db = b / f ** x
    while x < z:
        for i in range(y):
            x += 1
            print("{:3f}".format(x + 0 * f), end="  ")
        print()
    if x >= z:
        print("The relationship is concentric and the rule is equal")
    else:
        print("The relationship is not convergent and the rule is not equal")

# X should not be greater than 30 to 33

def Positive():
    while True:
        a = int(input("NUM:"))
        if -a + a == 0:
            b = -a + (-a)
            c = b * (-1)
            d = -a + c
            print("NUM:", -a)
            print("multiplication:", b)
            print("negative multiplication:", c)
            print("result:", d)

import numpy

import time

import tqdm

import math

import scipy

import matplotlib.pyplot as plt

import sympy

import fractions

import colorama

import pylj

def small_large_and_equal_operators(x, y):
    if x > y:
        print(x, ' is larger than', y)

    elif x < y:
        print(y, ' is larger than', x)

    elif x == y:
        print(x, ' is equal with', y)

def bump(x):
        a = x + 1
        print(a)
        print(a + 1)
        print(a + a + 1)
        print(a + a + a + 1)
        print(a + a + a + a + 1)
        print(a + a + a + a + a + 1)
        print(a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
        print(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)

# Fibonacci Series using Dynamic Programming
def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    FibArray = [0, 1]

    while len(FibArray) < n + 1:
        FibArray.append(0)

    if n <= 1:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = fibonacci(n - 1)

        if FibArray[n - 2] == 0:
            FibArray[n - 2] = fibonacci(n - 2)

    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]
    print(fibonacci(23))

def maxi():
    x = int(input("number of numbers:"))
    z = []
    for i in range(x):
        y = int(input('NUM:'))
        z.append(y)
    print(max(z))

def Count(n):
    print(n)
    Count(n+1)
    # Don't call this function (Count)

def factorial(n):
    if n == 0 or n == 1:
        F = 1
    else:
        F = 1
        for i in range(1, n + 1):
            F *= i
    print(F)

def Alpha_0_statement(n):
    x = 4*n - 1
    print(x, 'The first phase in Crowley''s group')
    y = x * (3*n + 1)
    print(y, 'The second phase of Crowley''s collection')
    z = y * (5*n / 1)
    print(z, 'The last phase of Crowley''s collection')
    print('This function is Crowley''s alpha-0 sum statement, which shows the phases one by one.')

def Binomial_analogy(n):
    x = n * n - n + n * (n * n - n + n) ^ (n * n - n + n)
    print(x)
    if n < x:
        print('True, ', x,'is greater than', n)
    elif n > x:
        print('False ', n,'is greater than', x)
    elif n == x:
        print('Equal ', n,'is Equal with',x)

def Unequal_argument(n):
    x = n + n
    y = x - n
    if y == n:
        print(True)
    else:
        print(False)

def Zayg_rule(n):
    x = n + n
    y = -n
    z = x = y
    print(x, y, z, z, '"E"' == True)

def math_lite():
    while True:
     x = int(input('ORACLE >'))
     y = int(input('ORACLE >'))
     z = input('OPERATOR >')
     if z == '+':
        print(x + y)
     elif z == '-':
        print(x - y, '1 mode')
        print(y - x, '2 mode')
     elif z == '*':
        print(x * y)
     elif z == '**':
        print(x ** y, '1 mode')
        print(y ** x, '2 mode')
     elif z == '/':
        print(x / y, '1 mode')
        print(y / x, '2 mode')
     elif z == '%':
        print(x % y, '1 mode')
        print(y % x, '2 mode')
     else:
         print(colorama.Fore.RED,'[Error]', colorama.Fore.RESET,colorama.Fore.WHITE,'<Unspecified entry>')

def Alpha_1(α, β):
    y = fractions.Fraction(α, α ^ 2)
    if β == y:
        print(y, '= β')
        print(β, 'Beta is Equal to alpha over alpha to the power of two')
    elif not β == y:
        print(y, '= β')
        print(β, 'Beta is Not Equal to alpha over alpha to the power of two.')
    print('\n',y == β)
    print('\nAlpha-1')

def Wrights_Theorem(α, β, Δ, θ):
     x = math.radians(α)
     y = math.sin(x)
     x2 = math.radians(β)
     y2 = math.sin(x2)
     x3 = math.radians(Δ)
     y3 = math.sin(x3)
     x4 = math.radians(θ)
     y4 = math.sin(x4)
     z = y - y2
     z2 = y2 - y3
     z3 = y3 - y4
     z4 = z * z2 - y
     z5 = z2 * z3 - y2
     z6 = z3 * z4 - y3
     z7 = z4 * z5 - y4
     Z = (z7 * z6 * z5 * z4) * (z7 * θ) * (z7 * θ)
     Z2 = Z - z7 - z6 - z5 - z4
     Z3 = Z2 * Z
     Z4 = Z3 * Z2
     Z5 = Z4 * Z3
     Z6 = Z5 * Z4 * Z3 * Z2 * Z - α - β - Δ - θ
     Z7 = Z6 * 2
     Z8 = Z7 * Z7 * Z7
     print(Z8)
     print('\n', α, β, Δ, θ, 'Up')
     x = math.radians(-α)
     y = math.sin(x)
     x2 = math.radians(-β)
     y2 = math.sin(x2)
     x3 = math.radians(-Δ)
     y3 = math.sin(x3)
     x4 = math.radians(-θ)
     y4 = math.sin(x4)
     z = -y - -y2
     z2 = -y2 - -y3
     z3 = -y3 - -y4
     z4 = -z * -z2 - -y
     z5 = -z2 * -z3 - -y2
     z6 = -z3 * -z4 - -y3
     z7 = -z4 * -z5 - -y4
     Z = (-z7 * -z6 * -z5 * -z4) * (-z7 * -θ) * (-z7 * -θ)
     Z2 = -Z - z7 - z6 - z5 - -z4
     Z3 = -Z2 * -Z
     Z4 = -Z3 * -Z2
     Z5 = -Z4 * -Z3
     Z6 = -Z5 * -Z4 * -Z3 * -Z2 * -Z - -α - -β - -Δ - -θ
     Z7 = -Z6 * 2
     Z8 = -Z7 * -Z7 * -Z7
     print('\n', Z8)
     print('\n', -α, -β, -Δ, -θ, 'Up')

def polyarea(n, a):
    area = (4 * math.pow(20, 2)) / (4 * math.tan(math.pi / 4))
    print(area)

def second_degree_equation(a, b, c):
    print('Solve the quadratic equation ax**2 + bx + c = 0')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        sol1 = (-b - math.sqrt(d)) / (2 * a)
        sol2 = (-b + math.sqrt(d)) / (2 * a)
        print('The solution are {0} and {1}'.format(sol1, sol2))
    elif d == 0:
        sol1 = -b // (2 * a)
        print('The solution is {0} '.format(sol1))
    else:
        print('The equation has no answer')

def Pythagorean_numbers(a, b, c):
    a = int(input("please Enter Number1: "))
    b = int(input("please Enter Number2: "))
    c = int(input("please Enter Number3: "))
    if a * a == b * b + c * c or b * b == c * c + a * a or c * c == a * a + b * b:
        print("Yes")
    else:
        print("No")

def Prime_number(n):
    n = int(input('please input your n: '))
    accumulator = 0
    for i in range(1, n + 1):
        if n % i == 0:
            accumulator += 1
    if accumulator == 2:
        print('your number is prime')
    else:
        print('your number is not prime')

def The_theorem_of_the_two_zeta_formula(ζ):
    ζ = sympy.zeta(ζ ^ ζ)
    β = ζ + ζ
    y = sympy.sqrt(ζ + math.pi ** ζ + β ** ζ ** ζ)
    sympy.pprint(expr=y, use_unicode=True)

def g_beta_alpha(ε):
    Δ = sympy.sqrt(ε + ε ^ ε)
    λ = sympy.divisor_sigma(ε,  ε ^ 2)
    φ = sympy.factorial(ε)
    β = sympy.sqrt(φ)
    α = sympy.sqrt(β)
    Σ = α * β / φ
    g = λ + φ + sympy.sqrt(Σ) - Δ
    sympy.pprint(g)

def obvious_infinite(δ):
    a = sympy.sqrt(δ)
    x = sympy.symbols('η')
    y = a * a
    z = sympy.symbols('π')
    λ = sympy.sin(a) / y
    τ = sympy.log(λ)
    b = sympy.sqrt(τ - sympy.sqrt(λ) * x + y / z + sympy.sqrt(δ))
    sympy.pprint(b)

def The_transformation_of_Zayg(ρ):
    Σ = sympy.rad(ρ)
    μ = Σ * sympy.sqrt(ρ)
    x = sympy.symbols('λ')
    y = sympy.symbols('π')
    z = sympy.symbols('Ω')
    β = sympy.sin(μ) / x * y
    sympy.pprint(β)
    print('β =', z)

def collectivization(x):
    y = sympy.symbols('ζ')
    z = sympy.symbols('Δ')
    a = x * sympy.simplify(x + 3 + y) / z
    sympy.pprint(a)
    sympy.pprint(a + 1)
    sympy.pprint(a + a + 1)
    sympy.pprint(a + a + a + 1)
    sympy.pprint(a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)
    sympy.pprint(a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + a + 1)

def Sulfurosis(Σ):
    b = sympy.symbols('η')
    b2 = sympy.symbols('β')
    a = sympy.digamma(Σ) / b
    c = a - sympy.sqrt(Σ) / b2
    λ = c * Σ
    sympy.pprint(λ)

def Masdelos(x):
    φ = x * x ^ x
    β = sympy.symbols('β')
    λ = sympy.symbols('Σ')
    y = sympy.symbols('λ')
    μ = (x * φ / β - φ / λ) / y
    sympy.pprint(μ)

def Power_of_Zayg(x):
    a1 = sympy.symbols('η')
    a2 = sympy.symbols('ε')
    a3 = sympy.symbols('λ')
    a = a3 - x * x * x / a1
    b = a / a2 ** 2
    sympy.pprint(b)

def Product_table(x, y):
    for i in range(1, x):
        for j in range(1, y):
            print("{:3d}".format(i * j), end=" ")
        print()
    # According to x, it is better not to make y bigger than 1 to n

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    print(sum == n)

def binomial(x, y, n, m, s):
    a = (x + y) ^ n
    while n < m:
        for i in range(s):
            n += 1
            print("{:3d}".format(x + y ^ n), end="  ")
        print()

def herman_law(n, n2, x):
    h = ((n * n) ^ (n * n) ^ n)
    β = n ^ h
    α = β ^ (β * β) ^ h
    y = α * α
    while n < n2:
       for i in range(x):
           n += 1
           print("{:3d}".format(((n * n) ^ (n * n) ^ n)), end="  ")
       print()
    # Correct calculation up to five zero digits (x)
    # Correct calculation up to five zero digits (n2)

def herman_logarithmic_expansion(x, x2, x3):
    while x < x2:
       for i in range(x3):
           x += 1
           print("{:3d}".format(x * x ^ (x * x) ^ x * x), end="  ")
       print()

class HermanCirclePrinciples:
    def principle1(x):
        a = float(input("your number  :"))
        c = a + a
        Δ = c * math.pi
        α = x * x ^ x
        β = α * α
        λ = sympy.symbols('λ')
        d = α * β * Δ - sympy.sqrt(math.pi) / λ
        sympy.pprint(d)

    def principle2(x, y):
        a = float(input("your number  :"))
        c = a + a
        b = c * math.pi
        d = b * x ** y / a
        print(d)

    def principle3(x, y, z):
        a = float(input("your number  :"))
        c = a + a
        b = c * math.pi
        d = b / sympy.sqrt(z) ** y
        sympy.pprint(d)

def three_addition(x, c, z, x2):
    while x < c:
        y = x + 3
        for i in range(z):
                x += 3
                print("{:3d}".format(x + 0), end="  ")
        print()
    x3 = int(input())
    if x3 == x2:
        print("\n", c, " > ", x3)
# input is equal to x2
# x2 is equal to x


def Check_whether_f_is_convergent_or_not(x, y, z):
    t = time.time()
    dt = x / t
    f = t + dt
    b = f ** math.e
    db = b / f ** x
    while x < z:
        for i in range(y):
            x += 1
            print("{:3f}".format(x + 0 * f), end="  ")
        print()
    if x >= z:
        print("The relationship is concentric and the rule is equal")
    else:
        print("The relationship is not convergent and the rule is not equal")

# X should not be greater than 30 to 33

def Positive():
    while True:
        a = int(input("NUM:"))
        if -a + a == 0:
            b = -a + (-a)
            c = b * (-1)
            d = -a + c
            print("NUM:", -a)
            print("multiplication:", b)
            print("negative multiplication:", c)
            print("result:", d)

