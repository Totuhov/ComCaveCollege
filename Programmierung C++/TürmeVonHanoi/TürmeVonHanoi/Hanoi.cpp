#include "Hanoi.h"
#include <iostream>

void Hanoi::ausgeben()
{
	// Scheiben ausgeben
	for (int zeile = 0; zeile < 3; zeile++)
	{
		for (int spalte = 0; spalte < 3; spalte++)
		{
			std::cout << hanoi[zeile][spalte] << "\t";
		}

		// Zeilenumbruch
		std::cout << std::endl;
	}	
}

void Hanoi::bewegen()
{
	// Position a (von)
	short von_a;

	// Position b (nach)
	short nach_b;

	// interaktive Eingabe
	std::cout << "\n";
	std::cout << "Von Position:  ";
	std::cin >> von_a;

	std::cout << "Nach Position: ";
	std::cin >> nach_b;


	// oberste Scheibe von Position von_a entfernen
	char Zeichen;
	int position_1, position_2;

	// - von oben nach unten in der Position von_a gehen
	for (int i = 0; i < 3; i++)
	{
		// Prüfung
		// Wenn der Inhalt ungleich leer ist, dann 1. Inhalt zwischenspeichern 
		//								       und 2. Inhalt auf leer setzen.
		// Wenn der Inhalt gleich leer ist, dann gehe ein Schritt nach unten.

		if (hanoi[i][von_a - 1] != ' ')
		{
			// Wenn der Inhalt ungleich leer ist

			// 1. Inhalt und Position zwischenspeichern
			Zeichen = hanoi[i][von_a - 1];
			position_1 = i;
			position_2 = von_a - 1;

			// 2. Inhalt auf leer setzen
			hanoi[i][von_a - 1] = ' ';

			// Abbruch, weil die oberste Scheibe entfernt wurde
			break;
		}

	}


	// Scheibe als neue oberste Scheibe bei nach_b ablegen
	// - von unten nach oben in der Position nach_b gehen
	for (int i = 2; i >= 0; i--)
	{
		// Prüfung:
		// Wenn der Inhalt gleich leer ist, dann die Scheiben hier ablegen
		// Wenn der Inhalt ungleich leer ist, dann gehe ein Schritt nach oben.
		if (i == 2 && hanoi[i][nach_b - 1] == ' ')
		{
			hanoi[i][nach_b - 1] = Zeichen;

			// Abbruch, weil die oberste Scheibe abgelegt wurde
			break;
		}
		else
			if (hanoi[i][nach_b - 1] == ' ')
			{
				if (hanoi[i + 1][nach_b - 1] < Zeichen)
				{
					std::cout << "Fehler.";

					// Zurücksetzen
					hanoi[position_1][position_2] = Zeichen;
				}
				else
					hanoi[i][nach_b - 1] = Zeichen;

				break;
			}
	}
	if (hanoi[0][0] == 'A' || hanoi[0][1] == 'A' || hanoi[0][2] == 'A')
		ziel = true;
}

bool Hanoi::GetZiel() 
{
	return ziel;
}
