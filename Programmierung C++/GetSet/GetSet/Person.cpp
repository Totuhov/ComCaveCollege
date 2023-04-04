#include <stdio.h>
#include <string>
#include "Person.h"

void Person::SetAlter(int alter) 
{
	this->alter = alter;

	fprintf(pfile, "%d", alter);
}

int Person::GetAlter()
{
	return alter;
}

Person::Person() 
{
	// Datei öffnen

	fopen_s(&pfile, "alter.txt", "a");
}

Person::~Person()
{
	// Datei schließen
	fclose(pfile);
}