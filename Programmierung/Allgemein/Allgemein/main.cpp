#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <fstream>
#include <string>
#include "info.h"
#include "CalculatorClass.h"
#include "PasswordCreator.h"
#include "hilfe.h"
#include "zahlenratten.h"
#include "random_number.h"
using namespace std;


int main()
{
	info_message();

	string input;

	while (input != "end")
	{
		cout << "/main->";
		cin >> input;

		if (input == "h")
		{
			hilfe();
		}
		else if (input == "t")
		{
			for (size_t i = 0; i < 1000; i++)
			{
				int a = random_number(1, 100);
				if (a > 100)
					cout << a << " !!!!!!!!!!\n";
				else
					cout << a << endl;
			}
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
		else if (input == "spiele")
		{
			string game;
			string line;
			ifstream myfile("games.txt");
			if (myfile.is_open())
			{
				while (getline(myfile, line))
				{
					cout << line << '\n';
				}
				myfile.close();
			}

			else cout << "Datei kann nicht geöffnet werden";

			cout << "main/spiele->";
			cin >> game;

			while (game != "r")
			{
				if (game == "z")
				{
					zahlenratten();

					cout << "main/spiele->";
					cin >> game;
				}
				else if (game == "h")
				{
					hilfe();
					cout << "main/spiele->";
					cin >> game;
				}

			}
		}

	}
	cout << "\nAuf Wiedersehen!\n";
	return(0);
}


