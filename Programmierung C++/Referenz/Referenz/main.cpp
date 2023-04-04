#include <iostream>

using namespace std;

int main()
{
	int i = 2;

	cout << "i = " << i << endl;
	cout << "&i = " << &i << endl;

	// Referenz

	int& ref = i;

	cout << "i = " << i << endl;
	cout << "&i = " << &i << endl;
	cout << "ref = " << ref << endl;
	cout << "&ref = " << &ref << endl;

	i = 7;

	cout << "i = " << i << endl;
	cout << "&i = " << &i << endl;
	cout << "ref = " << ref << endl;
	cout << "&ref = " << &ref << endl;

	ref = 82;

	cout << "i = " << i << endl;
	cout << "&i = " << &i << endl;
	cout << "ref = " << ref << endl;
	cout << "&ref = " << &ref << endl;

	int k = -123;

	cout << "k = " << k << endl;

	// ...

	ref = k;

	cout << endl << endl;
	cout << "i = " << i << endl;
	cout << "ref = " << ref << endl;
	cout << "k = " << k << endl;

	ref = 0;

	cout << endl << endl;
	cout << "i = " << i << endl;
	cout << "ref = " << ref << endl;
	cout << "k = " << k << endl;

	cout << "&k = " << &k << endl;

	return 0;
}