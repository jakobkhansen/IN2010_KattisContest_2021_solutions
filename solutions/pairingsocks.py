def main():
    org = list(map(int, input().split(' ')))
    aux = list()
    moves = 0

    while org:
        if aux and aux[-1] == org[-1]:
            aux.pop(); org.pop()
        else:
            aux.append(org.pop())
        moves += 1

    print("impossible" if aux else moves)


if __name__ == '__main__':
    input()
    main()
