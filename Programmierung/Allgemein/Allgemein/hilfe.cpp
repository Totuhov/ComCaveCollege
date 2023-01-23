#include <fstream>
#include <string>
#include <iostream>
using namespace std;

void hilfe()
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