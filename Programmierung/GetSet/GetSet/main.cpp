#include <iostream>
#include <vector>
#include "Person.h"

int main()
{
	Person person;

	std::cout << "Name: ";
	std::cin >> person.name;

	int alter;
	std::cout << "Alter: ";
	std::cin >> alter;

	person.SetAlter(alter);

	std::cout << "Der Mensch " << person.name << " ist " << person.GetAlter() << " Jahre alt.\n\n";

	std::vector<Person> persons(0);
	persons[0] = person;

	persons[persons.size()] = person;

	for (int i = 0; i < persons.size(); i++)
	{
		std::cout << persons[i].name << std::endl;

	}


	return 0;
}