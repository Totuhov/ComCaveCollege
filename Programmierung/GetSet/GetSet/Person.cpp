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
	// Datei �ffnen

	fopen_s(&pfile, "alter.txt", "a");
}

Person::~Person()
{
	// Datei schlie�en
	fclose(pfile);
}