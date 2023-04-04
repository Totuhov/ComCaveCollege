#include <iostream>
#include "CMensch.h"

int main()
{
	CMensch mensch;

	// Alter und Name eingeben
	std::cout << "Name: ";
	std::cin >> mensch.name;

	int alter;
	std::cout << "Alter: ";
	std::cin >> alter;
	mensch.SetAlter(alter);

	std::cout << "Der Mensch " << mensch.name << " ist " << mensch.GetAlter() << " Jahre alt.\n\n";

	return 0;
}
