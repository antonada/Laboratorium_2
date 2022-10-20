print("Ex 1")


def bin_to_dec(digit):

    dlina = len(digit)

    print(dlina)

    number_dec = 0

    for i in range(0, dlina):

        number_dec = number_dec + int(digit[i]) * (2 ** (dlina - i - 1))

    return number_dec


a = input("Please input number on two number system")

print("Naw we will convertation, number on ten number system = " + bin_to_dec(a))

print("____________________________________________________________________________________________________________")

print("Ex 2")

res = 0

n = float(input("Input first number on Horner algorytm"))

x = float(input("Input second number on Horner algorytm"))

while n > 0:

    coef = float(input())

    res += coef

    res *= x

    n -= 1

coef = float(input())

res += coef

print(res)

print("____________________________________________________________________________________________________________")

print("Ex 3")


