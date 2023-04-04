#include <iostream>

using namespace std;

void tausche_pointer(int* a, int* b, int* c)
{

	int temp;
	if (*a > *b) {
		temp = *a;
		*a = *b;
		*b = temp;
	}
	if (*a > *c) {
		temp = *a;
		*a = *c;
		*c = temp;
	}
	if (*b > *c) {
		temp = *b;
		*b = *c;
		*c = temp;
	}


}


void sortieren(int& x, int& y, int& z)
{
	int zahl1, zahl2, zahl3;
	if (x > y && x > z)
	{
		zahl1 = x;
		if (y > z){
			zahl2 = y;
			zahl3 = z;
		}
		else{
			zahl2 = z;
			zahl3 = y;
		}
	}
	else if (y > x && y > z){

		zahl1 = y;
		if (x > z)	{
			zahl2 = x;
			zahl3 = z;
		}
		else		{
			zahl2 = z;
			zahl3 = x;
		}
	}
	else	{

		zahl1 = z;
		if (x > y){
			zahl2 = x;
			zahl3 = y;
		}
		else{
			zahl2 = y;
			zahl3 = x;
		}
	}
	z = zahl1;
	y = zahl2;
	x = zahl3;

}

int main()
{
	int a, b, c;
	char i;

	while (true)
	{
		cout << "Zahl 1: ";
		cin >> a;
		cout << "Zahl 2: ";
		cin >> b;
		cout << "Zahl 3: ";
		cin >> c;

		//sortieren(a, b, c);
		tausche_pointer(&a, &b, &c);

		cout << a << " " << b << " " << c << "\n\n";

		cout << "für Wiederholung: 'j'";
		cin >> i;

		if (i != 'j')
		{
			break;
		}
	}


	return 0;
}