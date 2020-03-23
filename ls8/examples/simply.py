import sys

PRINT_BEEJ = 1     # all-caps defines this as a macro.
HALT       = 2
PRINT_NUM  = 3

memory = [
    PRINT_BEEJ,
    PRINT_NUM,
    1,
    PRINT_NUM,
    12,
    PRINT_BEEJ,
    PRINT_NUM,
    37,
    HALT
]

pc = 0                   # program counter: extremely fast memory
running = True

while running:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")

    elif command == HALT:
        running = False

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2

    else:
        print(f"unknown instruction: {command}")
        sys.exit(1)

    pc += 1
    
