def main():
    cs = input()
    stack = []
    all = [ "{", "[", "(", ")", "]", "}" ]
    opp = { "}": "{", ")": "(", "]": "[" }

    for i in range(len(cs)):
        if cs[i] in all[:3]:
            stack.append(cs[i])
        else:
            if cs[i] in all[3:]:
                if not stack or stack[-1] != opp[cs[i]]:
                    print(cs[i], i)
                    return
                stack.pop()

    print("ok so far")


if __name__ == "__main__":
    input()
    main()
