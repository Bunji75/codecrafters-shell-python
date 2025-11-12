import sys
import os

commands = ["exit", "echo", "type", "path"]


def checkPath(paths, command):
    for path in paths:
        if command in path:
            pathOfCommand = path
            return True, pathOfCommand
        else:
            return False, ''


def main():

    while (1):
        sys.stdout.write("$ ")
        command = input()
        pathseperator = os.pathsep
        paths = []
        foundInPath = False
        pathOfCommand = ''

        paths += os.getenv('PATH').split(pathseperator)

        if "type" in command:
            command = command.removeprefix("type ")
            foundInPath, pathOfCommand = checkPath(paths, command)
            if command in commands and foundInPath:
                print(f"{command} is {pathOfCommand}")
                continue
            elif command in commands:
                print(f"{command} is a shell builtin")
                continue
            else:
                print(f"{command.removeprefix("type ")}: not found")
                continue

        if "echo " in command:
            print(f"{command.removeprefix("echo ")}")

        if command == "exit 0":
            exit(0)
        else:
            if command in commands:
                print(f"{command} is a command but is incorrectly formatted")
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
