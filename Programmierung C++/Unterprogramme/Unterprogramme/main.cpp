#include <iostream>
#include "funk.h"

using namespace std;


int main() 
{
	char op;	
	double x, y;

	cout << "Gebe ein Wert von x: \n";
	cin >> x;
	cout << "operator: \n";
	cin >> op;
	cout << "Gebe ein Wert von y: \n";
	cin >> y;

	if (op == '+')
	{
		cout << add(x, y);
	}
	else if (op == '-')
	{
		cout << sub(x, y);
	}
	else if (op == '*')
	{
		cout << mult(x, y);
	}
	else if (op == '/')
	{
		cout << div(x, y);
	}

	return 0;
}