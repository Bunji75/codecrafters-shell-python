import sys


def main():

    while (1):
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            exit(0)
        if "echo" in command:
            print(f"{command.removeprefix("echo ")}")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
