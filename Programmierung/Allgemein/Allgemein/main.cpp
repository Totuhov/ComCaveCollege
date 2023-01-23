#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <fstream>
#include <string>
#include "info.h"
#include "CalculatorClass.h"
#include "PasswordCreator.h"
using namespace std;




int main()
{
	info_message();

	string input;

	while (input != "end")
	{
		cout << "->";
		cin >> input;

		if (input == "h")
		{
			string line;
			ifstream myfile("Help.txt");
			if (myfile.is_open())
			{
				while (getline(myfile, line))
				{
					cout << line << '\n';
				}
				myfile.close();
			}

			else cout << "Datei kann nicht geöffnet werden";
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

			else cout << "Datei kann nicht geöffnet werden";
		}
		else if (input == "p")
		{
			PasswordCreator create;
			cout << create.CreatePassword() << endl;

		}
		
	}

	cout << "\nAuf Wiedersehen!\n";
	return(0);
}


