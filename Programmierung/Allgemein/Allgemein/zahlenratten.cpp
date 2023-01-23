#include "random_number.h"
#include <string>
#include <iostream>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <fstream>
#include <numbers>


using namespace std;


void zahlenratten()
{
	string results[5];
	string names[5];
	string name;

	int punkte = 100;

	int r;
	r = random_number(1, 100);

	char tmBuff[30];
	int eingabe;

	string ratten = "Ratten Sie die Zahl: ";

	while (true)
	{
		cout << ratten;
		cin >> eingabe;

		ofstream myfile;

		myfile.open("zahlenraten_resultatent.txt", fstream::app);

		if (myfile.is_open())
		{
			auto start = std::chrono::system_clock::now();
			auto legacyStart = std::chrono::system_clock::to_time_t(start);
			ctime_s(tmBuff, sizeof(tmBuff), &legacyStart);
			myfile << "start " << tmBuff;
		}

		while (r != eingabe)
		{
			if (eingabe > r)
			{
				punkte--;
				//
				cout << "-Die Zahl ist kleiner als " << eingabe << endl;
				cout << ratten;
				cin >> eingabe;
				myfile << eingabe << ", ";
				continue;
			}
			else if (eingabe < r)
			{
				punkte--;
				//
				cout << "-Die Zahl ist größer als " << eingabe << endl;
				cout << ratten;
				cin >> eingabe;
				myfile << eingabe << ", ";
				continue;
			}
		}
		std::ifstream input_file("zahlenraten_resultatent.txt");

		std::string line;
		while (getline(input_file, line))
		{
			results.push_back(line);
		}

		{
			/*

			for (size_t i = 0; i < 5; i++)
			{
				if (punkte > results[i])
				{
					for (size_t i = 0; i < 5 - i - 1; i++)
					{
						results[4 - i] = results[4 - i - 1];
					}
					results[i] = punkte;
				}
				break;
			}

			cout << "Deine Name: ";
			cin >> name;

			for (int i : results) {
				myfile  << i << " Punkte - " << name << "\n";
			}*/
		}
		myfile << "( "<< eingabe << " )" << endl << "ende " << tmBuff << endl;
		if (myfile.is_open())
		{
			myfile.close();
		}
		cout << "Die Zahl ist gleich " << eingabe << endl;
		cout << "Noch einmal spielen (j/n)? ";

		string nochEine; cin >> nochEine;

		if (nochEine == "j")
		{
			continue;
		}
		else if (nochEine == "n")
		{
			break;
		}
	}
}