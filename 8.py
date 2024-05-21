import sys

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("ERROR")
        sys.exit()

def main():
    arguments = sys.argv[1:]
    file_name = arguments[-1]
    lines = read_file(file_name)

    if '--sort' in arguments:
        lines.sort()

    if '--num' in arguments:
        lines = [f"{i} {line}" for i, line in enumerate(lines)]

    for line in lines:
        print(line.strip())

    if '--count' in arguments:
        print(f"rows count: {len(lines)}")

if __name__ == "__main__":
    main()
