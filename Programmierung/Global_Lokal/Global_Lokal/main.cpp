#include <iostream>
using namespace std;

// Deklaration der globalen Variablen
int global = 1;

int fkt(int x = 3)
{
	for (int x = 4; x <= 5; x++)
	{
		cout << "x = " << x << endl;
	}
	int y = x;
	int z = x;

	x = 3;
	y = 4;
	z = 5;

	return y;
}

int main()
{
	//Deklaration der lokalen Variablen
	int lokal = 2;

	int x = 3;

	x = global;

	cout << "x = " << x << endl;

	x = fkt(x);

	cout << "x = " << x << endl;

	return 0;
}