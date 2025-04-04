from os import system, name

def clear_screen():
        system("cls" if name == "nt" else "clear")

def spacing(clear=False, lines=1):
    """
    Print empty lines for spacing.
    :param lines: Number of empty lines to print.
    """

    if clear:
        clear_screen()

    for _ in range(lines):
        print()


def main():
  
    spacing(clear=True, lines=5)

    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    appleIndex = fruit_list.index("apple")
    fruit_list.insert(appleIndex, "cherry")
    print(f"insert cherry: {fruit_list}")

    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    fruit_list.pop()
    print(f"pop orange: {fruit_list}")

    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    fruit_list.clear()
    print(f"cleared: {fruit_list}")

    spacing(lines=5)
    print("Have a blessed day!")
    spacing(lines=5)

if __name__ == "__main__":
    main()