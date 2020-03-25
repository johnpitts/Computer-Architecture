import sys

if len(sys.argv) != 2:
    print("usage: file.py filename")
    sys.exit(1)


filename = sys.argv[1]

try:
    with open(filename) as f:
        for line in f:
            print(line)

            # Ignore comments
            comment_split = line.split("#")

            # Strip out whitespace
            num = comment_split[0].strip()

            if num == '':
                continue

            print(num)
            val = int(num)

except FileNotFoundError:
    print("file not found")
    sys.exit(2)

str = "10000010"
int(str)
int(str, 2)  # gets integer from base 2 if str variable is a binary
