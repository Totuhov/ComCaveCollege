#include "Mensch.h"

string Mensch::GetVorname()
{
	return vorname;
}
void Mensch::SetVorname(string vorname)
{
	this->vorname = vorname;
}
string Mensch::GetNachName()
{
	return nachname;
}
void Mensch::SetNachname(string nachname)
{
	this->nachname = nachname;
}
int Mensch::GetAlter()
{
	return alter;
}
void Mensch::SetAlter(int alter)
{
	this->alter = alter;
}
