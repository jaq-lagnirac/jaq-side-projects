# Justin Caringal
# A throw-away joke that Dr. Anton Weisstein made while I 
# was sitting in on that I turned into a reality in 20 mins

OPTIONS = """---Weisstein's Worst Nightmare---

\tDISCLAIMER: Does not recognize errors in input

1) zero to 0 [alphabet-binary to binary]
2) 0 to zero [binary to alphabet-binary]

0) EXIT

"""
while True:
    try:
        option = int(input(OPTIONS))
    except:
        print('Non-numeric input recognized.')

    output = ''

    if option == 0:
        print('Thanks for using Weisstein\'s Worst Nightmare!')
        break

    elif option == 1:
        user_input = input('Input alphabet-binary string: ').lower()
        for i, _ in enumerate(user_input):
            if user_input[i:i+4] == 'zero':
                output += '0'
            elif user_input[i:i+3] == 'one':
                output += '1'
            else:
                pass

    elif option == 2:
        user_input = input('Input binary string: ')
        for x in user_input:
            if x == '0':
                output += 'ZERO'
            elif x == '1':
                output += 'ONE'
            else:
                output += '[ERROR]'
    
    else:
        print('Input not recognized')
    
    print(output, '\n')
