#include <iostream>
#include "CMensch.h"
#include "CStudent.h"
#include "CDozent.h"
#include "CMitarbeiter.h"
using namespace std;

int main()
{
	////////////////////////////////////////////////////////////////////
	// Objekt der Elternklasse
	CMensch person;

	string name;
	short alter;

	cout << "Mensch:\n";
	// Vorname
	cout << "Bitte gib deinen Vornamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	person.SetVorname(name);


	// Nachname
	cout << "Bitte gib deinen Nachnamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	person.SetNachname(name);


	// Alter
	cout << "Bitte gib dein Alter an: ";
	cin >> alter;

	// Wert an die Klasse übergeben
	person.SetAlter(alter);
	////////////////////////////////////////////////////////////////////////////


	// Daten entweder für Student, Dozent oder Mitarbeiter

	///////////////////////////////////////////////////////////////////////////
	// Student
	CStudent student1;

	cout << "Student:\n";
	// Vorname
	cout << "Bitte gib deinen Vornamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	student1.SetVorname(name);

	// Nachname
	cout << "Bitte gib deinen Nachnamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	student1.SetNachname(name);

	// Alter
	cout << "Bitte gib dein Alter an: ";
	cin >> alter;

	// Wert an die Klasse übergeben
	student1.SetAlter(alter);

	// Semester
	cout << "Bitte gib dein Semester an: ";
	cin >> alter;

	student1.SetSemester(alter);


	///////////////////////////////////////////////////////////////////////////
	// Dozent
	CDozent dozent1;

	cout << "Dozent:\n";
	// Vorname
	cout << "Bitte gib deinen Vornamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	dozent1.SetVorname(name);

	// Nachname
	cout << "Bitte gib deinen Nachnamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	dozent1.SetNachname(name);

	// Alter
	cout << "Bitte gib dein Alter an: ";
	cin >> alter;

	// Wert an die Klasse übergeben
	dozent1.SetAlter(alter);

	// Lehrbefaehigung
	char lehr;
	cout << "Lehrbefaehigung (j/n): ";
	cin >> lehr;

	/*
	if (lehr == 'j')
		dozent1.SetLehrbefaehigung(true);
	else
		dozent1.SetLehrbefaehigung(false);
	*/

	dozent1.SetLehrbefaehigung(lehr == 'j');


	///////////////////////////////////////////////////////////////////////////
	// Mitarbeiter
	CMitarbeiter mitarbeiter1;

	cout << "Mitarbeiter:\n";
	// Vorname
	cout << "Bitte gib deinen Vornamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	mitarbeiter1.SetVorname(name);

	// Nachname
	cout << "Bitte gib deinen Nachnamen an: ";
	cin >> name;

	// Wert an die Klasse übergeben
	mitarbeiter1.SetNachname(name);

	// Alter
	cout << "Bitte gib dein Alter an: ";
	cin >> alter;

	// Wert an die Klasse übergeben
	mitarbeiter1.SetAlter(alter);

	// Gehalt
	double gehalt;
	cout << "Gehalt: ";
	cin >> gehalt;

	mitarbeiter1.SetGehalt(gehalt);


	// Ausgabe der Daten
	cout << person.GetVorname() << " " << person.GetNachname() << " ist " << person.GetAlter() << " Jahre alt." << endl;

	cout << student1.GetVorname() << " " << student1.GetNachname() << " ist " << student1.GetAlter() << " Jahre alt." << endl;
	cout << "Semester: " << student1.GetSemester() << endl;

	cout << dozent1.GetVorname() << " " << dozent1.GetNachname() << " ist " << dozent1.GetAlter() << " Jahre alt." << endl;
	if (dozent1.GetLehrbefaehigung())
		cout << "Lehrbefaehigung: Ja" << endl;
	else
		cout << "Lehrbefaehigung: Nein" << endl;

	cout << mitarbeiter1.GetVorname() << " " << mitarbeiter1.GetNachname() << " ist " << mitarbeiter1.GetAlter() << " Jahre alt." << endl;
	cout << "Gehalt: " << mitarbeiter1.GetGehalt() << endl;

	return 0;
}