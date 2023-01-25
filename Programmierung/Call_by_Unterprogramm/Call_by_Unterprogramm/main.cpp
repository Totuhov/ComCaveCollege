#include <iostream>

using namespace std;

void tauschen_value(int x, int y)
{
	int temp = x;
	x = y;
	y = temp;
}
void tauschen_pointer(int* x, int* y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

void tauschen_reference(int& x, int& y)
{
	int temp = x;
	x = y;
	y = temp;
}

int main()
{
	int a = 5;
	int b = 10;

	cout << "a = " << a << "\tb = " << b << endl << endl;;

	// Tauschen
	// call by value
	// es werden die werte der beiden variablen a und b übergeben

	tauschen_value(a, b);

	cout << "a = " << a << "\tb = " << b << endl << endl;

	// call by pointer
	// es werden die Adressen der Variablen a und b übergeben

	tauschen_pointer(&a, &b);

	cout << "a = " << a << "\tb = " << b << endl << endl;

	// call by reference
	//

	tauschen_reference(a, b);

	cout << "a = " << a << "\tb = " << b << endl << endl;

	return 0;
}