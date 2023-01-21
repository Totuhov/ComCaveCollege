#include <iostream>
#include <string>
#include <sstream>
#include <set>
using namespace std;

class Start
{
public:
	void Info()
	{
		cout << "Welcome to c++" << endl;
		cout << "Tip: you can use 'h' for help\n\n";
	}
};

class Calculator
{
public:
	void Calculate()
	{
		string again;
		double result = 0;

		string error1 = "You can use only numbers to calculate!\n";
		string error2 = "Invalid operator!\n";

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
				cout << "Cannot divide by 0\n";
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
		}
	}
	bool is_number(const string& s)
	{
		long double ld;
		return((std::istringstream(s) >> ld >> std::ws).eof());
	}
};


int main()
{
	Start start;
	start.Info();
	string input;

	while (input != "end")
	{
		cout << "->";
		cin >> input;

		if (input == "h")
		{
			cout << "   c' - Calculator\n";
			cout << "  'r' - Return\n";
			cout << "'end' - Exit\n";
		}
		else if (input == "c")
		{
			Calculator calc;
			calc.Calculate();
		}
	}
	return(0);
}


