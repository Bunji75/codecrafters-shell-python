import sys
import os
import subprocess

commands = ["exit", "echo", "type", "path", "pwd", "cd"]


def checkPathForExe(paths, command):
    for path in paths:
        if os.path.exists(path):
            with os.scandir(path) as it:
                for entry in it:
                    if (not entry.name.startswith('.') and
                            entry.is_file() and
                        command == entry.name and
                            os.access(entry.path, os.X_OK)):
                        return True, entry.path
    return False, ''


def main():

    while (1):
        sys.stdout.write("$ ")
        userCommand = input()
        args = userCommand.split()
        count = 0
        for arg in args:
            count = count + 1

        pathseperator = os.pathsep
        paths = []
        foundInPath = False
        pathOfCommand = ''

        paths += os.getenv('PATH').split(pathseperator)
        foundInPath, commandPath = checkPathForExe(paths, args[0])

        if args[0] == "exit" and count > 1:
            exit(0)

        if args[0] == "type" and count > 1:
            foundInPath, pathOfCommand = checkPathForExe(paths, args[1])
            if args[1] in commands:
                print(f"{args[1]} is a shell builtin")
                continue
            elif foundInPath:
                print(f"{args[1]} is {pathOfCommand}")
                continue
            else:
                print(f"{args[1]}: not found")
                continue

        if args[0] == "echo":
            args.pop(0)
            print(" ".join(args))
            continue

        if args[0] == "pwd":
            print(os.getcwd())
            continue

        if args[0] == "cd":
            if os.access(args[1], os.F_OK):
                os.chdir(args[1])
            else:
                print(f"cd: {args[1]}: No such file or directory")
            continue

        if foundInPath and args[0] not in commands:
            subprocess.run(args)
            continue

        else:
            if args[0] in commands:
                print(f"{args[0]} is a command but is incorrectly formatted")
                continue
            else:
                print(f"{args[0]}: command not found")
                continue


if __name__ == "__main__":
    main()
