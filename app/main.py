import sys

commands = ["exit", "echo", "type"]


def main():

    while (1):
        sys.stdout.write("$ ")
        command = input()
        if command == "exit 0":
            exit(0)
        if "echo" in command:
            print(f"{command.removeprefix("echo ")}")
        if "type" in command:
            if command.removeprefix("type ") in commands:
                print(f"{command.removeprefix("type ")} is a shell builtin")
            else:
                print(f"{command.removeprefix("type ")}: not found")

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
