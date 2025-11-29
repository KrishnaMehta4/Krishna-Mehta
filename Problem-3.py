def main():
    try:
        a = int(input("Enter a (positive integer): ").strip())
        if a <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    top = a if a % 2 == 1 else a - 1
    result = [i for i in range(1, top + 1, 2)]
    print(", ".join(map(str, result)))

if __name__ == "__main__":
    main()
