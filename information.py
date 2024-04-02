'''
 * @author Anh Huy Nguyen
 * */
'''

import function

NAME = "ANH HUY NGUYEN"
ID = "110328330"
EMAIL = "nguay089"

# Print the nor function
def NOR_table():
    print("NOR")
    print("x y Z")
    print("-----")
    for i in range(2):
        for j in range(2):
            print(f"{i} {j} {int(function.NOR(i, j))}")

# Print the single-bit addition table
def ADD_table():
    print("ADDITION")
    print("c x y Z C")
    print("---------")
    for c in range(2):
        for x in range(2):
            for y in range(2):
                print(f"{c} {x} {y} {int(function.ADD_BIT(x, y, c))} {
                      int(function.CARRY_BIT(x, y, c))}")

# Complete and print the single-bit subtraction table 
def SUB_table():
    print("SUBTRACTION")
    print("b x y Z B")
    print("---------")
    for b in range(2):
        for x in range(2):
            for y in range(2):
                print(f"{b} {x} {y} {int(function.SUB_BIT(x, y, b))} {
                      int(function.BORROW_BIT(x, y, b))}")

# Complete and print the single-bit less than table
def LESS_table():
    print("LESS_THAN")
    print("l x y L")
    print("-------")
    for l in range(2):
        for x in range(2):
            for y in range(2):
                print(f"{l} {x} {y} {int(function.LESS_THAN(x, y, l))}")

# This function is used to call the truth tables of NOR, ADDITION, SUBTRACTION and LESS THAN functions.
def print_tables():
    NOR_table()
    print()
    ADD_table()
    print()
    SUB_table()
    print()
    LESS_table()
    
# This function is used to print my student's information and the university's guidelines.
def print_info():
    print(f"Author: {NAME}")
    print(f"Student ID: {ID}")
    print(f"EmailID: {EMAIL}")
    print("This is my own work as defined by the University's Academic Integrity Policy\n")
