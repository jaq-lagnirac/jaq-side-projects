// Justin Caringal
// an iterative implementation of the collatz conjecture

#include <iostream>
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
 * @return int : the user-defined value that will be used for the conjecture
 */
int get_user_input();


int main()
{
    cout << DESCRIPTION;
    int test = get_user_input();
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
        cout << "Give me an integer: ";
        cin >> input_num;
    }

    int cleaned_input = stoi(input_num);
    cout << cleaned_input << " success!";
    return cleaned_input;
}