import sys


def decode(n):
    n = int(n)

    length = 0
    while n >= 256**length:
        n -= 256**length
        length += 1

    res = ""
    for i in range(length-1, -1, -1):
        tmp = (int((n//(256**i)) % 256))
        res += chr(tmp)

    return res


def encode(program):
    length = 0

    res = 0
    length = len(program)

    for i in range(length-1, -1, -1):
        res += (256 ** (length - i - 1)) * (ord(program[i]) + 1)

    return res


if __name__ == "__main__":
    if len(sys.argv) == 2:
        estr = encode(sys.argv[1])
        print(f'encoded: {estr}')
        print(f'decoded: {decode(estr)}')
