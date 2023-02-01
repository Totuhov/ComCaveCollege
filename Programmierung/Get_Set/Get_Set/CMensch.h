#pragma once
#include <string>

class CMensch
{
private:
	// int alter = 0;
	short int alter = 0;

public:
	// string ist eine Klasse
	std::string name = "";

public:
	// Deklaration der Get- und Set-Methoden
	void SetAlter(int alter);
	int GetAlter();

	CMensch();
	~CMensch();

	// Datei-Handler
	FILE* pfile;
};

