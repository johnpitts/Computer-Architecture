import sys

PRINT_BEEJ     = 1     # all-caps defines this as a macro.
HALT           = 2
PRINT_NUM      = 3
SAVE           = 4
PRINT_REGISTER = 5   
ADD            = 6   # regA += regB

memory = [
    PRINT_BEEJ,
    SAVE,
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT
]

register = [0] * 8        # each register can hold a "word" which is = to bits computer is rated

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

    elif command == SAVE:
        num = memory[pc +1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2

    elif command == ADD:
        reg_a = memory[pc +1]
        reg_b = memory[pc +2]
        register[reg_a] += register[reg_b]
        pc += 3

    else:
        print(f"unknown instruction: {command}")
        sys.exit(1)

    pc += 1
    


# registers: small and fastest, very expensive
# cache: bigger by a little (a few MB), slightly slower, really expensive
# RAM: much much bigger, slower, decently expensive compared to hard drives. 64 GB
# HDD/SSD: hard drive or Solid State Drive "disc, tape". A Terabyte
# Cloud storage, very very massive, super slow.