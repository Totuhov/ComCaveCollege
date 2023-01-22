#pragma once
#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <fstream>
#include <string>
using namespace std;


class CalculatorClass
{
public:
	void Calculate()
	{
		string again;
		double result = 0;

		string error1 = "You can use only numbers to calculate!\n";
		string error2 = "Invalid operator!\n";
		string error3 = "Cannot divide by 0\n";

		cout << "<< Calculator >>\n\n" << "available operators: + - * /\n\n";

		while (again != "y")
		{

			cout << "first number: ";
			string one; cin >> one;

			if (!is_number(one))
			{
				cout << error1;
				continue;
			}

			cout << "operator: ";
			char op; cin >> op;

			if (op != '+' && op != '-' && op != '*' && op != '/')
			{
				cout << error2;
				continue;
			}

			cout << "second number: ";
			string  two; cin >> two;

			if (!is_number(two))
			{
				cout << error1;
				continue;
			}

			if (op == '/' && stod(two) == 0)
			{
				cout << error3;
				continue;
			}

			switch (op)
			{
			case '+':
				result = stod(one) + stod(two);
				break;
			case '-':
				result = stod(one) - stod(two);
				break;
			case '*':
				result = stod(one) * stod(two);
				break;
			default:
				result = stod(one) / stod(two);
			}

			cout << one << " " << op << " " << two << " = " << result << endl;

			cout << "Exit Calculator? y/n\n";
			cin >> again;

			while (again != "y" && again != "n")
			{
				cout << "'y' for exit OR 'n' to continue calculation\n";
				cin >> again;
			}
		}
	}
	bool is_number(const string& s)
	{
		return !s.empty() && std::find_if(s.begin(),
			s.end(), [](unsigned char c) { return !std::isdigit(c); }) == s.end();
	}
};