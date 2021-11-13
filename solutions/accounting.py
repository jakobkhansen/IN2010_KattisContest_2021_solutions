from collections import defaultdict

def main():
    _, q = map(int, input().split(' '))
    m = defaultdict(lambda: "0")

    for _ in range(q):
        cmd = input().split(' ')
        if cmd[0] == "SET":
            m[cmd[1]] = cmd[2]
        elif cmd[0] == "RESTART":
            tmp = cmd[1]
            m = defaultdict(lambda: tmp)
        elif cmd[0] == "PRINT":
            print(m[cmd[1]])


if __name__ == "__main__":
    main()
