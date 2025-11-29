"""
Problem-2: Print first 'a' odd numbers
Input: integer a >= 1
Output: list of odd numbers separated by comma
Example:
  Input: 4
  Output: 1, 3, 5, 7
"""
def main():
    try:
        a = int(input("Enter a (positive integer): ").strip())
        if a <= 0:
            print("Please enter an integer greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    odds = [2*i + 1 for i in range(a)]
    print(", ".join(str(x) for x in odds))

if __name__ == "__main__":
    main()
