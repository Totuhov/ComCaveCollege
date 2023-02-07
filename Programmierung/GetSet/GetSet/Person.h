#pragma once
#include <string>

class Person
{
private:
	short int alter = 0;

public:
	std::string name = "";

public:
	void SetAlter(int alter);
	int GetAlter();	

public:
	Person();
	~Person();
	FILE* pfile;
};


