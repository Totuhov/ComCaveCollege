#pragma once

class Hanoi
{
	char hanoi[3][3] = { {'A', ' ', ' '},
					 {'B', ' ', ' '},
					 {'C', ' ', ' '}
	};
	bool ziel = false;

public:
	void ausgeben();
	void bewegen();
	bool GetZiel();
};

