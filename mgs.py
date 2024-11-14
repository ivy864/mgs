import sys


def decode(n):
    n = int(n)

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

    for i in range(length-1, -1, -1):
        res += (2 * 256**i) + ord(program[i])

    return res


if __name__ == "__main__":
    encoded = encode("Hi, this is a test!")
    print(encoded)
    print(decode(encoded))
