#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    if length < 4 or length > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if length == 4:
        operators = {'+': add, '-': sub, '*': mul, '/': div}
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        answer = operators[op](a, b)
        print("{} {} {} = {}".format(a, op, b, answer))
