// Justin Caringal
// an iterative implementation of the collatz conjecture

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

const string DESCRIPTION = {"\t\t---Collatz Conjecture---\n\n"
    "\t Program by J. Caringal\n\nUnder the rules"
    "\n\t-If the number is even, divide it by two"
    "\n\t-If the number is odd, triple it and add one"
    "\nwill every positive integer eventually transform into 1?\n\n"
    "Iterative C++ implementation.\n\n"};


/**
 * @brief checks to see if inputted string is a valid integer
 * 
 * @param input the string to be tested
 * @return true if input is valid integer
 * @return false if input is not an integer
 */
bool check_int(string input);

/**
 * @brief Get the user input and validates input
 * 
 * @return int the user-defined value that will be used for the conjecture
 */
int get_user_input();


/**
 * @brief Performs the collatz conjecture on input num
 * 
 * @param input_num the starting number for the conjecture
 * @return unsigned the number of operations performed to reach 1
 */
unsigned collatz_iterative(int input_num);


int main()
{
    std::cout << DESCRIPTION;
    
    // user input for num
    int input_num = get_user_input();

    // main driver function for collatz
    unsigned iteration_count = collatz_iterative(input_num);

    if (iteration_count == 1)
    {
        std::cout << "It took 1 iteration to reach 1." << endl;
    }
    else
    {
        std::cout << "It took " << iteration_count << " iterations to reach 1." << endl;
    }
    std::cout << "Exiting program.";
}


bool check_int(string input)
{
    // iterates through entire string
    for (size_t index = 0; index < input.length(); index++)
    {
        // checks each character to see if it's valid
        if (isdigit(input[index]) == false)
        {
            return false;
        }
    }

    // all of the chars in the string are digits,
    // therefore it's a valid int
    return true;
}


int get_user_input()
{
    // declares input variable, initializes with placeholder
    string input_num = "DUMMY";

    // main driving loop for user input
    while (!check_int(input_num))
    {
        // prompts user to give input
        std::cout << "Give me an integer: ";
        cin >> input_num;
    }

    // coverts str to int and returns
    int cleaned_input = stoi(input_num);
    return cleaned_input;
}


unsigned collatz_iterative(int input_num)
{
    unsigned counter = 0;

    while (input_num != 1)
    {
        counter++;
        if (input_num % 2 == 0) // even
        {
            input_num /= 2;
        }
        else // odd
        {
            input_num = (3 * input_num) + 1;
        }

        std::cout << left << setw(5) << counter << input_num << endl;
    }

    return counter;
}