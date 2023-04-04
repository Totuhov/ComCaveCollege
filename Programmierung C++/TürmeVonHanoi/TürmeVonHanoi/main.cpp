#include <iostream>
#include "Hanoi.h"

int main()
{
	Hanoi hanoi;

	do
	{
		hanoi.ausgeben();

		hanoi.bewegen();
	} 
	while (!hanoi.GetZiel());
	
	std::cout << std::endl;
	hanoi.ausgeben();

	// Ausgabe des Glückwunsches
	std::cout << "\nGlückwunsch. Du hast das Ziel erreicht.\n\n";


	return 0;
}