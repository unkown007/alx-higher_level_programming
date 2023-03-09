#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv) - 1
    print("{} {}".format(
        size,
        "argument:" if size == 1 else (
            "arguments." if size == 0 else "arguments:")))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
