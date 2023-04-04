#include <iostream>
#include "Student.h"
#include "ITStudent.h"
#include "MultimediaStudent.h"

using namespace std;

int main()
{
	ITStudent itStudent;

	MultimediaStudent mStudent;

	string a = mStudent.GetBetriebssystem();

	string name;

	cout << "Geben Sie bitte die Name des Studentes ein: ";
	cin >> name;

	mStudent.SetName(name);


	cout << "Name: "  <<mStudent.GetName()  << " mit Betriebssystem " << a;

	return 0;
}