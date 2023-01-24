#include <iostream>

using namespace std;

int main()
{
	int i = 5;

	cout << "i = " << i << endl;

	cout << "Adresse von i = " << &i << endl;

	int* p = 0x0;

	cout << "p = " << p << endl;

	cout << "Adresse von p = " << &p << endl;

	p = &i;

	cout << "Der Wert von p = " << p << endl;

	cout << "i = " << i << endl;

	cout << "*p = " << *p << endl;

	i = -7;

	cout << "i = " << i << endl;

	cout << "*p = " << *p << endl;

	*p = 38;

	cout << "i = " << i << endl;

	cout << "*p = " << *p << endl;

	return 0;
}