#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])

    if sign == '+':
        cal = add(a, b)
    elif sign == '-':
        cal = sub(a, b)
    elif sign == '*':
        cal = mul(a, b)
    elif sign == '/':
        cal = div(a, b)
    else:
        error = "Unknown operator. Available operators: +, -, * and /"
        print("{}".format(error))
        exit(1)

    print("{} {} {} = {}".format(a, sign, b, cal))
