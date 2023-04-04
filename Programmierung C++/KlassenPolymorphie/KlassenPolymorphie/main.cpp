#include <iostream>
#include "Person.h"
#include "Student.h"
#include "Tier.h"
#include "Hund.h"

using namespace std;

int main()
{
	Person* person = new Student;

	Person* personsList[5];

	personsList[0] = person;

	Tier* tier = new Hund;

	tier->SetAlter(1);

	cout << tier->GetAlter();

	return 0;
}