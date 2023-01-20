#include <iostream>
using namespace std;

int main()



{
    double operand1, operand2, ergebniss;
    char operatorSymbol;



    cout << "Operand1: ";
    cin >> operand1;



    cout << "Operator (+ - * /): ";
    cin >> operatorSymbol;



    cout << "Operand2: ";
    cin >> operand2;

    if (operand2 == 0 && operatorSymbol == '/')
    {
        cout << "Computer sagt nö!";
    }

    switch (operatorSymbol)
    {
    case '+':
        ergebniss = operand1 + operand2;
        break;
    case '-':
        ergebniss = operand1 - operand2;
        break;
    case '*':
        ergebniss = operand1 * operand2;
        break;
    case '/':
        ergebniss = operand1 / operand2;
        break;

    }



    std::cout << operand1 << " " << operatorSymbol << " " << operand2 << " = " << ergebniss << std::endl;



    return 0;
}