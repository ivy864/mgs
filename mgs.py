import sys


def decode(n):
    n = int(n)
    print(n)
    length = 0
    while n >= 256**length:
        n -= 256**length
        length += 1
    res = ""
    for i in range(length-1, -1, -1):
        tmp = chr(int((n//(256**i)) % 256))
        res += tmp

    return res


def encode(program):
    res = 0
    length = len(program)

    return res


if __name__ == "__main__":
    print(encode("Hi, this is a test!"))
    print(decode(209180605381204854470575573749277224))
