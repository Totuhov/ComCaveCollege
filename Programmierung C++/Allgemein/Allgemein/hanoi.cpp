#include <iostream>

char Hanoi[3][3] = { {'A', ' ', ' '},
					 {'B', ' ', ' '},
					 {'C', ' ', ' '}
};

bool Ziel = false;
int zuege = 0;

void ausgeben()
{
	// Scheiben ausgeben
	for (int zeile = 0; zeile < 3; zeile++)
	{
		for (int spalte = 0; spalte < 3; spalte++)
		{
			std::cout << Hanoi[zeile][spalte] << "\t";
		}

		// Zeilenumbruch
		std::cout << std::endl;
	}

	// Position ausgeben
	std::cout << "\n1\t2\t3" << "\t" << "Zuege: " << zuege << '\n';
}


// ausgeben2(Zeiger)

void bewegen()
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
	int altePositionX, altePositionY;

	// - von oben nach unten in der Position von_a gehen
	for (int i = 0; i < 3; i++)
	{
		// Prüfung
		// Wenn der Inhalt ungleich leer ist, dann 1. Inhalt zwischenspeichern 
		//								       und 2. Inhalt auf leer setzen.
		// Wenn der Inhalt gleich leer ist, dann gehe ein Schritt nach unten.

		if (Hanoi[i][von_a - 1] != ' ')
		{
			// Wenn der Inhalt ungleich leer ist

			// 1. Inhalt zwischenspeichern
			Zeichen = Hanoi[i][von_a - 1];

			// 2. Inhalt auf leer setzen
			Hanoi[i][von_a - 1] = ' ';

			altePositionX = i;
			altePositionY = von_a - 1;

			// Abbruch, weil die oberste Scheibe entfernt wurde
			break;
		}

	}


	// Scheibe als neue oberste Scheibe bei nach_b ablegen
	// - von unten nach oben in der Position nach_b gehen
	for (int i = 2; i >= 0; i--)
	{
		// Prüfen ob erlaubt ist


		if (i < 2 && ((int)Hanoi[i + 1][nach_b - 1] < (int)Zeichen))
		{
			std::cout << "\n" << "Oops!" << std::endl;
			Hanoi[altePositionX][altePositionY] = Zeichen;
			break;

		}

		// Prüfung:
		// Wenn der Inhalt gleich leer ist, dann die Scheiben hier ablegen
		// Wenn der Inhalt ungleich leer ist, dann gehe ein Schritt nach oben.
		if (Hanoi[i][nach_b - 1] == ' ')
		{
			Hanoi[i][nach_b - 1] = Zeichen;

			zuege++;

			// Abbruch, weil die oberste Scheibe abgelegt wurde
			break;
		}
	}

	// Ziel erreicht
	// Ziel des Spiels ist es, den kompletten Scheiben-Stapel vom linken Stab auf den rechten Stab zu versetzen. Wikipedia
	if (Hanoi[0][2] == 'A')
		Ziel = true;
}

int hanoi()
{
	// Array Hanoi deklarieren
	// 3 Positionen
	// Höhe 3
	// Werte sind 'A', 'B' und 'C'
	// Array Hanoi mit Ausgangswerten initialisieren
	/*
	char Hanoi[3][3] = { {'A', ' ', ' '},
						 {'B', ' ', ' '},
						 {'C', ' ', ' '}
					   };
	*/

	// Ziel erreicht?
	// false: Ziel noch nicht erreicht
	// true:  Ziel erreicht
	// bool Ziel = false;

	std::cout << "Ziel des Spiels ist es, den kompletten Scheiben-Stapel vom linken Stab auf den rechten Stab zu versetzen.\n\n";

	do
	{
		// Aufruf
		ausgeben();

		bewegen();
	} while (!Ziel);

	std::cout << std::endl;
	ausgeben();

	// Ausgabe des Glückwunsches
	std::cout << "\nGlueckwunsch. Du hast das Ziel erreicht.\n\n";


	return 0;
}