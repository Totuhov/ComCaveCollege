#include <stdio.h>
#include "CMensch.h"

void CMensch::SetAlter(int alter)
{
	// die lokale Variable alter (Parameter)
	// �berdeckt die Klassenvariable alter,
	// da beide denselben Namen besitzen.
	// L�sung:
	// 1. Namen der lokalen Variablen (Parameter) umbenennen oder
	// 2. Verwende den this-Zeiger
	this->alter = alter;

	// Alter in die Datei schreiben
	// C-Funktion fprintf()
	// das erste f steht f�r file
	// das zweite f steht f�r Formatierung
	fprintf(pfile, "%d", alter);
	// fputs("hallo", pfile);
}

int CMensch::GetAlter()
{
	return alter;
}

CMensch::CMensch()
{
	// Datei �ffnen

	// fopen = Datei �ffnen
	// pfile = Datei-Handler
	// "alter.txt" = Name der Datei
	// "w" = write (schreiben)
	fopen_s(&pfile, "alter.txt", "w");
}

CMensch::~CMensch()
{
	// Datei schlie�en
	fclose(pfile);
}