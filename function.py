'''
 * @author Anh Huy Nguyen
 * */
'''

#   This function will take the user inputs from keyboard. 
def get_input():
    option = input("Choose operation [+, -, q]: ")
    while option not in ['+', '-', 'q']:
        print("Invalid operation.\n")
        option = input("Choose operation [+, -, q]: ")
    return option

#   Check if an user's input is a binary number.
def _is_valid(binary:str) -> bool:
    for bit in binary:
        if bit != '1' and bit != '0':
            return False
    return True

#   Return statement if an input is a binary number or not.
def ask_binary(prompt:str)-> str:
    while True:
        result = input(prompt)
        if _is_valid(result):
            return result.lstrip('0')
        print("Not a binary number!")

def NOR(x,y):
    # NOR function with NOR = !(x||y)
    return not (x or y)   

def ADD_BIT(x,y,c):
    # Add x,y as bits, c as carrier
    # Does not handle overflow
    return XOR(XOR(x,y),c)

def XOR(x, y):
    # XOR function for x,y as int
    return not(NOR(NOR(x,NOR(x,y)), NOR(y, NOR(x, y))))

def CARRY_BIT(x,y,c):
    # Adding 3 bits
    # Only handle carrier
    return bool((x and y) or (c and XOR(x, y)))

def SUB_BIT(x,y,b):
    # Sub x,y as bits, b as borrow
    # Does not handle overflow
    return XOR(XOR(x, y), b)

def BORROW_BIT(x,y,b):
    # Only handle carrier
    return bool((not x and y) or (b and not XOR(x, y)))

def LESS_THAN(x,y,l):
    # Check if x is less than y
    # l is result from previous pair
    # L = ((!x AND y) OR (!x OR y) AND l))
    # L = Nor(nor(!x,y),nor(!x||y),l))
    return bool(NOR(NOR(not x, y), NOR(not x or y, l)))



    

