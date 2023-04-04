#include <iostream>
#include "Person.h"


void Person::SetVorname()
{
	std::cout << "Vorname: ";
	std::cin >> Vorname;
}


void Person::SetNachname()
{
	std::cout << "Nachname: ";
	std::cin >> Nachname;
}


void Person::SetAlter()
{
	std::cout << "Alter: ";
	std::cin >> Alter;
}
