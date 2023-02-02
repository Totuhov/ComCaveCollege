#include "Student.h"
#pragma once
class ITStudent : public Student
{
	string programierSprache;

public:
	void SetProgramierSprache(string sprache);
	string GetProgramierSprache();
};

