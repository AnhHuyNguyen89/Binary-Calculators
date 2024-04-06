'''
 * @author Anh Huy Nguyen
 * */
'''
import function
import information


def add_binary(x:str,y:str) ->str:
    # Ensure both strings are the same length by padding the shorter string with leading zeros
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    
    C = 0
    Z = []
    # Add two bitstrings
    for i in range(max_len-1,-1,-1):
        z = str(int(function.ADD_BIT(int(x[i]),int(y[i]),C)))
        Z.insert(0,z)
        C = int(function.CARRY_BIT(int(x[i]),int(y[i]),C))
    # If there is carry bit remaining, add 1 to result
    if C == 1:
        Z.insert(0,'1')
        
    return ''.join(Z)


#This function is used to calculate the subtraction of two binaries. 
def minus_binary(x:str, y:str) -> str:

    # Ensure both strings are the same length by padding the shorter string with leading zeros
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    B = 0
    L = 0
    Z = []

    # Check if x < y or not
    for i in range(max_len-1,-1,-1):   
        L = function.LESS_THAN(int(x[i]), int(y[i]),L)
    # Calculate
    for i in range(max_len-1,-1,-1):   
        # Swap if x < y to prevent negative
        if  L:    
            z = str(int(function.SUB_BIT(int(y[i]),int(x[i]),B)))
            B    = int(function.BORROW_BIT(int(y[i]),int(x[i]),B))
        # If not, do the normal function
        else:
            z = str(int(function.SUB_BIT(int(x[i]),int(y[i]),B)))
            B    = int(function.BORROW_BIT(int(x[i]),int(y[i]),B))
        Z.insert(0,z)

    Z = ''.join(Z).lstrip('0')

    # If x < y, the result is negative
    if function.LESS_THAN(x,y,L):
        Z='-' + Z

    return Z


def main():
    
    # Show the author information and the truth table of addition, subtraction or less than. 
    information.print_info()
    information.print_tables()

    # Here is Making a loop that prompt a user can choose either "+" for addition or "-" for subtraction,
    # if user chooses "q" and the program ends
    while True:

        ACCEPTED = ['+', '-', 'q']  # Operations
        op = input(f"Choose operation {ACCEPTED}: ") 

        match op:
            # Case "+": The addition between two binary numbers X & Y
            case '+':
                # Check if the prompt input is valid
                x = function.ask_binary('X: ')
                y = function.ask_binary('Y: ')

                # Check if input numbers are over 80 bits
                max_len = max(len(x),len(y)) + 2

                print(f'  {x.rjust(max_len," "):>}')
                print(f'+ {y.rjust(max_len," "):>}')
                print('-'*(max_len + 2))
                result = add_binary(x,y) # RESULT
                print(f'  {result.rjust(max_len," "):>}')

            # Case "-": The subtraction between two binary numbers X & Y
            case '-':
                # Check if the prompt input is valid
                x = function.ask_binary('X: ')
                y = function.ask_binary('Y: ')

                # Check if input numbers are over 80 bits
                max_len_minus = max(len(x),len(y)) + 2

                print(f'  {x.rjust(max_len_minus," "):>}')
                print(f'- {y.rjust(max_len_minus," "):>}')
                print('-'*(max_len_minus + 2))
                result = minus_binary(x,y)  # RESULT
                print(f'  {result.rjust(max_len_minus," "):>}')

            # Case "q": Quit program
            case 'q':
                break

            # Check if the input is invalid
            case _:
                print('Invalid operation')
                continue

if __name__=='__main__':
    main()