#include <iostream>
#include "Person.h"

int main()
{
	Person personen[25];
	char eingabe;

	std::string task = "Die Daten eingeben. \n\n";
	std::string wiederholen = "Moechten Sie die Daten einer anderen Person schreiben? j/n ";

	for (int i = 0; i < 25; i++)
	{
		std::cout << task;

		Person person;

		person.SetVorname();
		person.SetNachname();
		person.SetAlter();

		personen[i] = person;

		std::cout << wiederholen;
		std::cin >> eingabe;

		if (eingabe != 'j')
		{
			std::cout << std::endl;
			break;
		}
	}

	for (int i = 0; i < 25; i++)
	{
		if (personen[i].Alter == -1)
		{
			break;
		}
		std::cout << "Alter - " << personen[i].Alter << " / Vorname - " << personen[i].Vorname << " / Nachname - " << personen[i].Nachname << std::endl;
	}

	return 0;
}