#include <iostream>

int main()
{
	double zahl;
	std::cout << "Geben Sie ein Zahl: ";
	std::cin >> zahl;

    int zahl2 = std::abs(zahl);
	

	if (zahl == zahl2)
	{
		std::cout << zahl << " ist eine gerade Zahl\n";
	}
	else
	{
		std::cout << zahl << " ist eine ungerade Zahl\n";
	}
}