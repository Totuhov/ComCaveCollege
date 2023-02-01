#include <iostream>

// Klasse definieren
// CPerson ist ein Datentyp (eine Hülle)
class CPerson
{
	// Hier werden die Member angegeben!


	// alter ist eine Klassen-Variable,
	// die nur in dieser Klasse (Hülle) existiert
public:
	int alter = 0;
	double koerpergroesse;
private:
	double gewicht;
protected:
	char geschlecht;

public:
	// Deklaration und Implementierung
	void SetAlter(int alt)
	{
		alter = alt;
	}

	// Deklaration
	int GetAlter();
};

// Objekt person1 ist eine globale Variable
CPerson person1;

int main()
{
	// Objekt person deklarieren
	// person ist eine lokale Variable
	CPerson patrick;

	patrick.alter = 18;
	patrick.koerpergroesse = 185;

	std::cout << "Patrick ist " << patrick.alter << " Jahre alt.\n";
	std::cout << patrick.koerpergroesse << std::endl;


	CPerson nikolay;
	nikolay.alter = 19;
	nikolay.koerpergroesse = 180;

	person1.alter = 29;


	// Eingabe des Alters
	int alter;

	std::cout << "Alter: ";
	std::cin >> alter;

	// Aufruf der Methode
	nikolay.SetAlter(alter);

	std::cout << "Nikolay ist jetzt " << nikolay.GetAlter() << std::endl;

	return 0;
}

// Implementierung der Methode außerhalb der Klassen-Definiion
int CPerson::GetAlter()
{
	return alter;
}
