#include <iostream>

class Mensch
{
public:
	Mensch() { std::cout << "Konstruktor von Mensch\n"; }
	~Mensch() { std::cout << "Destruktor von Mensch\n"; }
};

class Student : public Mensch
{
public:
	Student() { std::cout << "Konstruktor von Student\n"; }
	~Student() { std::cout << "Destruktor von Student\n"; }
};


int main()
{
	// Objekt erstellen
	Student student;

	// Objekt zerstören
	return 0;
}