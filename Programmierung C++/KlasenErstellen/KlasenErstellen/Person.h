#pragma once
#include <string>
class Person
{

public:
	std::string Vorname;
	std::string Nachname;
	int Alter = -1;
	void SetVorname();
	void SetNachname();
	void SetAlter();
};

