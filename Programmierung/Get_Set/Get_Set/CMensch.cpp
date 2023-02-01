#include <stdio.h>
#include "CMensch.h"

void CMensch::SetAlter(int alter)
{
	// die lokale Variable alter (Parameter)
	// überdeckt die Klassenvariable alter,
	// da beide denselben Namen besitzen.
	// Lösung:
	// 1. Namen der lokalen Variablen (Parameter) umbenennen oder
	// 2. Verwende den this-Zeiger
	this->alter = alter;

	// Alter in die Datei schreiben
	// C-Funktion fprintf()
	// das erste f steht für file
	// das zweite f steht für Formatierung
	fprintf(pfile, "%d", alter);
	// fputs("hallo", pfile);
}

int CMensch::GetAlter()
{
	return alter;
}

CMensch::CMensch()
{
	// Datei öffnen

	// fopen = Datei öffnen
	// pfile = Datei-Handler
	// "alter.txt" = Name der Datei
	// "w" = write (schreiben)
	fopen_s(&pfile, "alter.txt", "w");
}

CMensch::~CMensch()
{
	// Datei schließen
	fclose(pfile);
}