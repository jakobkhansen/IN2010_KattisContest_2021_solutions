def main():
    left = 1
    right = 1000
    
    while left <= right:
        guess = (left + right) // 2
        print(guess)
    
        s = input()
        if s == "higher":
            left = guess + 1
        elif s == "lower":
            right = guess - 1
        else:
            exit()


if __name__ == "__main__":
    main()
