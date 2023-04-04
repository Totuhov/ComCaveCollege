#include <iostream>
using namespace std;

int main()
{
	int i = 7;
	char c = 'E';
	double d = 3.14;

	void* Array[3] = { &i, &c, &d };

	cout << Array[0] << "\t" << *(int*)Array[0] << endl;;
	cout << Array[1] << "\t" << *(char*)Array[1] << endl;;
	cout << Array[2] << "\t" << *(double*)Array[2] << endl;;

	return 0;
}

