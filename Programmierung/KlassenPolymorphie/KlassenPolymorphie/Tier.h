#pragma once
#include <string>

using namespace std;

 class Tier
{
protected:
	int alter = 18;
	string name;

public:
	virtual void SetName(string name)
	{
		this->name = name;
	}
	virtual string GetName()
	{
		return this->name;
	}

	virtual void SetAlter(int alter)
	{
		this->alter = alter;
	}
	virtual int GetAlter()
	{
		return this->alter;
	}
};

