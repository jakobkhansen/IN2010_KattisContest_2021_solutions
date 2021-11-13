def main():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    boxes = list(map(int, input().split(' ')))

    # Fill boxes
    for i in range(len(boxes)):
        if boxes[i]:
            tree[boxes[i]].append(i+1)

    # Standard BFS on every box
    for _ in range(int(input())):
        queries = list(map(int, input().split(' ')))[1:]
        visited = set()

        while queries:
            curr = queries.pop()
            visited.add(curr)
            for b in tree[curr]:
                if b not in visited:
                    queries.append(b)

        print(len(visited))


if __name__ == '__main__':
    main()
