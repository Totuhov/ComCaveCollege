#pragma once
#include <iostream>
#include "Mensch.h"

using namespace std;

class Ich
{
	string Vorname;
	string Nachname;
	int Alter;

	Mensch Vater;
	Mensch Mutter;
	Mensch Kinder[5];
};

