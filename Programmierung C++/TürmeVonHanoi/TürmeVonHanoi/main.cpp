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

	// Ausgabe des Gl�ckwunsches
	std::cout << "\nGl�ckwunsch. Du hast das Ziel erreicht.\n\n";


	return 0;
}