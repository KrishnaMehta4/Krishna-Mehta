def parse_list(s: str):
    items = [x.strip() for x in s.replace(",", " ").split()]
    numbers = []
    for it in items:
        try:
            numbers.append(int(it))
        except ValueError:
            pass
    return numbers

def main():
    default = "1,2,8,9,12,46,76,82,15,20,30"
    user = input(f"Enter numbers separated by comma (press Enter to use default {default}): ").strip()
    nums = parse_list(user) if user else parse_list(default)

    counts = {}
    for d in range(1, 10):
        counts[d] = sum(1 for n in nums if n % d == 0)
    print(counts)

if __name__ == "__main__":
    main()
