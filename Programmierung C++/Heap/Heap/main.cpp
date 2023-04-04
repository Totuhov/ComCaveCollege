#include <iostream>

using namespace std;

void prozedur()
{
	cout << "Wert = ";
}

int main()
{
	// Heap Variablen deklarieren
	int* p;

	// Hier wird Speicherplatz (Hier 4 Byte wegen int) auf dem Heap reserviert
	p = new int;

	*p = 6;

	// Speicherplatz auf dem Heap freigeben
	delete p;

	// Wie kann der Heap (Zeiger p) ab die prozedur übergeben werden?
	prozedur();

	return 0;
}