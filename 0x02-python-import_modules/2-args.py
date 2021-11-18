#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = 0
    length = len(argv)
    if length == 1:
        print("{} arguments.".format(count))
    elif length == 2:
        print("{} argument:".format(length - 1))
        print("{}: {}".format(length - 1, argv[1]))
    elif length > 2:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            count += 1
            print("{}: {}".format(count, argv[i]))
