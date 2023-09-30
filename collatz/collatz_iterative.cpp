// Justin Caringal
// an iterative implementation of the collatz conjecture

#include <iostream>
#include <string>

using namespace std;

const string DESCRIPTION = "\t\t---Collatz Conjecture---\n\n"
    "\t Program by J. Caringal\n\nUnder the rules"
    "\n\t-If the number is even, divide it by two"
    "\n\t-If the number is odd, triple it and add one"
    "\nwill every positive integer eventually transform into 1?\n\n"
    "Iterative C++ implementation.\n\n";

int main()
{
    cout << DESCRIPTION;
}