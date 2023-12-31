# Justin Caringal
# an iterative implementation of the collatz conjecture

DESCRIPTION = '''\t\t---Collatz Conjecture---

\t Program by J. Caringal

Under the rules
\t-If the number is even, divide it by two
\t-If the number is odd, triple it and add one
will every positive integer eventually transform into 1?

Iterative Python implementation.

'''

def get_user_input():
    """Gets user input
    
    A function to organize user input and validation

    Args:
        None

    Returns:
        int: Returns the number to be used in the conjecture
    """

    # bool flag to ask for inputs
    is_int = False

    while not is_int:
        # prompts user for integer
        input_num = input('Give me an integer: ')

        # converts str input into int
        try:
            manipulated_num = int(input_num)
        except:
            print('Input not accepted, try again.')
            continue

        is_int = True # is ignored if exception handling sends loop to top

    return manipulated_num


def collatz_iterative(manipulated_num):
    """Implements collatz
    
    A function that implements an iterative implementation
    of the collatz conjecture
    
    Args:
        manipulated_num (int): A user-defined number
        
    Returns:
        int: returns the number of operations performed
    """

    # implements iteration counter (the number of
    # operations performed before reaching 1)
    counter = 0

    # main driving loop
    while manipulated_num != 1:
        
        # increments counter
        counter += 1

        if manipulated_num % 2 == 0: # even
            manipulated_num /= 2
        else: # odd
            manipulated_num = (3 * manipulated_num) + 1
        
        # truncates posibility of floats into an int
        manipulated_num = int(manipulated_num)

        print(f'{counter : <5}{manipulated_num}')
    
    return counter


def main():
    """ THE MAIN FUNCTION """

    print(DESCRIPTION)

    # input num
    manipulated_num = get_user_input()

    # main driver function for collatz
    counter = collatz_iterative(manipulated_num)

    if counter == 1:
        print('It took 1 iteration to reach 1.')
    else:
        print(f'It took {counter} iterations to reach 1.')
    
    print('Exiting program.')


if __name__ == '__main__':
    main()