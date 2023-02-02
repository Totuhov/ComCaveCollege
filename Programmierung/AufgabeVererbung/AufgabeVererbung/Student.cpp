#include "Student.h"
#include <string>


void Student::SetName(string name)
{
	this->name = name;
}
string Student::GetName()
{
	return name;
}
void Student::SetAlter(int alter)
{
	this->alter = alter;
}
int Student::GetAlter()
{
	return alter;
}