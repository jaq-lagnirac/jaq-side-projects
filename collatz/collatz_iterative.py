# Justin Caringal
# an iterative implementation of the collatz conjecture

def main():
    """ THE MAIN FUNCTION """

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

        print(manipulated_num)

    if counter == 1:
        print('It took 1 iteration to reach 1.')
    else:
        print(f'It took {counter} iterations to reach 1.')
    
    print('Exiting program.')

if __name__ == '__main__':
    main()