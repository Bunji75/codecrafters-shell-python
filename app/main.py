import sys


def main():

    while (1):
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            print("0")
            break
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
