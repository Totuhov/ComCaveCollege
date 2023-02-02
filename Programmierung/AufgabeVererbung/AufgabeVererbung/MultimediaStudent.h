#include "Student.h"
#pragma once
class MultimediaStudent : public Student
{
	string betriebssystem;

public:
	void SetBetriebssystem(string system);
	string GetBetriebssystem();
};

