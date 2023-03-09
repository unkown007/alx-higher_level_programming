#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    new = ""
    res = ""
    for i in range(1, len(sys.argv)):
        size_i = len(sys.argv[i])
        size_r = len(res)
        if size_r == 0:
            for k in range(size_i - 1, -1, -1):
                res = sys.argv[i][k] + res
        else:
            size_r = size_r - 1
            size_i = size_i - 1
            rem = 0
            s = 0
            new = ""
            while size_i >= 0 and sys.argv[i][size_i] != '-':
                if (sys.argv[i][0] == '-' and res[0] != '-') or\
                        (sys.argv[i][0] != '-' and res[0] == '-'):
                    x = int(sys.argv[i][size_i]) + rem
                    if int(res[size_r]) >= x:
                        s = int(res[size_r]) - x
                        rem = 0
                    else:
                        s = (int(res[size_r]) + 10) - x
                        rem = 1
                else:
                    rem = int(s / 10)
                    s = int(sys.argv[i][size_i]) + int(res[size_r]) + rem
                new = chr((s % 10) + ord('0')) + new
                size_i = size_i - 1
                size_r = size_r - 1
                if size_r < 0 or res[size_r] == '-':
                    break
            while size_i >= 0 and sys.argv[i][size_i] != '-':
                rem = int(s / 10)
                s = int(sys.argv[i][size_i]) + rem
                new = chr((s % 10) + ord('0')) + new
                size_i = size_i - 1
            while size_r >= 0 and res[size_r] != '-':
                rem = int(s / 10)
                s = int(res[size_r]) + rem
                new = chr((s % 10) + ord('0')) + new
                size_r = size_r - 1
            if rem > 0:
                new = chr((rem) + ord('0')) + new
            if sys.argv[i][0] == '-' and res[0] == '-':
                new = '-' + new
            res = new
    print(res)
