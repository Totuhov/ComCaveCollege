#pragma once
#include <string>
using namespace std;

class CMensch
{
private:
	// string ist eine Klasse
	string Vorname;
	string Nachname;

	short Alter;

public:
	void SetVorname(string SVorname);
	void SetNachname(string SNachname);
	void SetAlter(short SAlter);
	string GetVorname();
	string GetNachname();
	short GetAlter();
};

