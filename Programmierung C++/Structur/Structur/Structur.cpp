#include <iostream>

using namespace std;

int main()
{
	struct dt_person
	{
		int alter = 32;
		char geschlaecht = 'd';
		short kinderAnzahl = 2;
	};

	dt_person Person1;

	Person1.alter = 32;
	Person1.geschlaecht = 'm';
	Person1.kinderAnzahl = 2;

	dt_person Person2 = {22, 'w', 0};

	cout << Person2.alter << " Jahre" << endl;

	struct mensch
	{
		int alter = 32;
		char geschlaecht = 'd';
		short kinderAnzahl = 2;
	} Mensch1, Mensch2;

	cout << "Mensch2: " << Mensch2.alter << " Jahre" << endl;;

	struct dt_structurFeld
	{
		int alter;
		char geschlaecht;
	};

	dt_structurFeld Klasse[3];

	Klasse[0].alter = 18;
	Klasse[0].geschlaecht = 'm';

	Klasse[1].alter = 17;
	Klasse[1].geschlaecht = 'w';

	Klasse[2].alter = 18;
	Klasse[2].geschlaecht = 'w';

	for (size_t i = 0; i < sizeof(Klasse) / sizeof(Klasse[0]); i++)
	{
		cout << Klasse[i].alter << "\t" << Klasse[i].geschlaecht << endl;
	}

	//------------------------------------------------------------------------

	struct dt_Mensch
	{
		int kinderanzahl;
		char geschlaecht_kinder[2];
	}Mensch;

	Mensch.kinderanzahl = 2;
	Mensch.geschlaecht_kinder[0] = 'm';
	Mensch.geschlaecht_kinder[1] = 'w';

	//-----------------------------------------------------------------------

	char arrayName[10]{ 'H', 'a', 'l', 'l', 'o', ' ', 'W', 'e', 'l', 't'};

	for (int i = 0; i < 10; i++)
	{
		cout << arrayName[i];
	}
	cout << endl;

	for (size_t i = 0; i < 10; i++)
	{
		cout << i + 1<< " Zeichen: ";
		cin >> arrayName[i];
	}

	for (int i = 0; i < 10; i++)
	{
		cout << arrayName[i];
	}
	cout << endl;

	cout << arrayName;

	return 0;
}
