def main():
    n = int(input().split(' ')[1])
    p = dict()
    stdo = 0

    for _ in range(n):
        cmd = input().split(' ')
        if cmd[0] == "SET":
            p[cmd[1]] = cmd[2]
        elif cmd[0] == "RESTART":
            p = dict()
            stdo = cmd[1]
        elif cmd[0] == "PRINT":
            try:
                print(p[cmd[1]])
            except:
                print(stdo)


if __name__ == "__main__":
    main()
