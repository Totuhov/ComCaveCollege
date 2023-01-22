#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <fstream>
#include <string>
#include "TestClass.h"
#include "CalculatorClass.h"
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

//class Calculator
//{
//public:
//	void Calculate()
//	{
//		string again;
//		double result = 0;
//
//		string error1 = "You can use only numbers to calculate!\n";
//		string error2 = "Invalid operator!\n";
//
//		cout << "<< Calculator >>\n\n" << "available operators: + - * /\n\n";
//
//		while (again != "y")
//		{
//
//			cout << "first number: ";
//			string one; cin >> one;
//
//			if (!is_number(one))
//			{
//				cout << error1;
//				continue;
//			}
//
//			cout << "operator: ";
//			char op; cin >> op;
//
//			if (op != '+' && op != '-' && op != '*' && op != '/')
//			{
//				cout << error2;
//				continue;
//			}
//
//			cout << "second number: ";
//			string  two; cin >> two;
//
//			if (!is_number(two))
//			{
//				cout << error1;
//				continue;
//			}
//
//			if (op == '/' && stod(two) == 0)
//			{
//				cout << "Cannot divide by 0\n";
//				continue;
//			}
//
//			switch (op)
//			{
//			case '+':
//				result = stod(one) + stod(two);
//				break;
//			case '-':
//				result = stod(one) - stod(two);
//				break;
//			case '*':
//				result = stod(one) * stod(two);
//				break;
//			default:
//				result = stod(one) / stod(two);
//			}
//
//			cout << one << " " << op << " " << two << " = " << result << endl;
//
//			cout << "Exit Calculator? y/n\n";
//			cin >> again;
//		}
//	}
//	bool is_number(const string& s)
//	{
//		long double ld;
//		return((std::istringstream(s) >> ld >> std::ws).eof());
//	}
//};


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
			string line;
			ifstream myfile("C:\\Users\\CC-Student\\Documents\\GitHub\\ComCaveCollege\\Programmierung\\Allgemein\\Allgemein\\Help.txt");
			if (myfile.is_open())
			{
				while (getline(myfile, line))
				{
					cout << line << '\n';
				}
				myfile.close();
			}

			else cout << "Unable to open file";
		}
		else if (input == "c")
		{
			CalculatorClass calc;
			calc.Calculate();
		}
		else if (input == "loops")
		{
			string line;
			ifstream myfile("Loops.txt");
			if (myfile.is_open())
			{
				while (getline(myfile, line))
				{
					cout << line << '\n';
				}
				myfile.close();
			}

			else cout << "Unable to open file";
		}
		else if (input == "test")
		{
			TestClass test = TestClass();
			cout << test.Message();
		}
	}

	cout << "\nGoodbye!\n";
	return(0);
}


