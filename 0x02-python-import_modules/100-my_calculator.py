#!/usr/bin/python3

def calculator():
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    ops = sys.argv[2]
    if ops != '+' and ops != '-' and ops != '*' and ops != '/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if ops == '+':
        ans = add(a, b)
    if ops == '-':
        ans = sub(a, b)
    if ops == '*':
        ans = mul(a, b)
    if ops == '/':
        ans = div(a, b)
    print('{} {} {} = {}'.format(a, ops, b, ans))


if __name__ == "__main__":
    calculator()
