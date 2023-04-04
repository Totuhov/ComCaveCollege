#include <string>

using namespace std;

#pragma once
class Student
{
private:
	string name;
	int alter;

public:
	void SetName(string name);
	string GetName();
	void SetAlter(int alter);
	int GetAlter();
};

