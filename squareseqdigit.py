def squareSequenceDigit(n, m):
    n = n - 1
    result = []
    while m != 0:
        m, d = divmod(m, 10)
        result.append(int(d))

    result.reverse()

    print(result[n])


if __name__ == "__main__":
    print(squareSequenceDigit(1, 1224765432))
    print(squareSequenceDigit(2, 7482901))
    print(squareSequenceDigit(7, 74283091))
    print(squareSequenceDigit(12, 14916253649648121144))
    print(squareSequenceDigit(17, 12345678909765432123456789))
    print(squareSequenceDigit(27, 123456789012345678901223456789023456789))
