# Justin Caringal
# a recursive implementation of the collatz conjecture

DESCRIPTION = '''\t\t---Collatz Conjecture---

\t Program by J. Caringal

Under the rules
\t-If the number is even, divide it by two
\t-If the number is odd, triple it and add one
will every positive integer eventually transform into 1?

Recursive Python implementation.

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


def collatz_recursive(num, counter):
    """Primary conjecture function
    
    The main function that performs the
    conjecture's operations, recursive
    
    Args:
        num: the input number which operations will be performed on
        counter: the a totalling of the number of iterations performed
        
    Returns:
        int: The number of operations performed
    """

    # truncates posibility of floats into an int
    num = int(num)

    # base case, ends recursion
    if num == 1:
        return counter
    
    counter += 1
    print(f'{counter : <5}{num}')

    # performs conjecture arthimetic
    if num % 2 == 0: # even
        num /= 2
    else: # odd
        num = (3 * num) + 1

    # sends recursion down the line
    return collatz_recursive(num, counter)


def collatz_driver(seed):
    """Collatz driver function
    
    A driver function to organize the recursive functions
    
    Args:
        seed (int): the starting number for the conjecture
        
    Returns:
        int: returns the number of operations performed
    """

    # implements iteration counter (the number of
    # operations performed before reaching 1)
    counter = 0

    # calculates iterations performed, performs conjecture operations
    iterations_performed = collatz_recursive(seed, counter)
    return iterations_performed


def main():
    """ THE MAIN FUNCTION """

    print(DESCRIPTION)

    # input num
    manipulated_num = get_user_input()

    iterations_performed = collatz_driver(manipulated_num)

    if iterations_performed == 1:
        print('It took 1 iteration to reach 1.')
    else:
        print(f'It took {iterations_performed} iterations to reach 1.')
    
    print('Exiting program.')


if __name__ == '__main__':
    main()