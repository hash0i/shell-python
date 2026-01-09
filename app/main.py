import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    valid_commands = {'help'}

    sys.stdout.write("$ ")
    
    command = input()
    if command is not None and command not in valid_commands:
        print(f"{command}: command not found")
        
    elif command == "exit":
        exit

if __name__ == "__main__":
    main()
