#include <iostream>
using namespace std;

int main()
{
	char feld[3][3];

	for (int i = 0; i < 3; i++)
	{
		for (int k = 0; k < 3; k++)
		{
			feld[i][k] = 32;
		}
	}

	char a = 'A';
	char b = 'B';
	char c = 'C';

	feld[2][0] = c;
	feld[1][0] = b;
	feld[0][0] = a;

	feld[2][1] = a;
	feld[0][0] = ' ';
	feld[1][1] = b;
	feld[1][0] = ' ';
	feld[1][0] = c;
	feld[2][0] = ' ';
	

	feld[2][2] = c;
	feld[1][0] = ' ';
	feld[1][2] = b;
	feld[1][1] = ' ';
	feld[0][2] = a;
	feld[1][2] = ' ';


    std::cout << "Hello World!\n";
}
