def one():
    print(7)

def two(arr):
    if arr[0] > arr[1]:
        print("Bigger")
    elif arr[0] == arr[1]:
        print("Equal")
    else:
        print("Smaller")


def three(arr):
    print(sorted(arr[:3])[1])


def four(arr):
    print(sum(arr))


def five(arr):
    print(sum(filter(lambda x: x % 2 == 0, arr)))


def six(arr):
    print("".join(map(lambda x: chr(x+97), map(lambda y: y % 26, arr))))


def seven(arr, n, curr=0):
    visited = set()

    while True:
        curr = arr[curr]

        if (curr > (n-1)):
            print("Out")
            return
        elif (curr == (n-1)):
            print("Done")
            return
        elif curr in visited:
            print("Cyclic")
            return
            
        visited.add(curr)


def main():
    n, t = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    
    # if you have python 3.10 =< you can use match-case instead
    if t == 1:
        one()
    elif t == 2:
        two(arr)
    elif t == 3:
        three(arr)
    elif t == 4:
        four(arr)
    elif t == 5:
        five(arr)
    elif t == 6:
        six(arr)
    else:
        seven(arr, n)


if __name__ == "__main__":
    main()
