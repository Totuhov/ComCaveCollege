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
	string name;
	cout << "Geben Sie Ihre Name ein: ";
	cin >> name;

	int punkte = 100;

	int r;
	r = random_number(1, 100);

	char tmBuff[30];
	int eingabe;

	string ratten = "Ratten Sie die Zahl: ";

	while (true)
	{
		ofstream myfile;
		myfile.open("zahlenraten_resultatent.txt", fstream::app);

		if (myfile.is_open())
		{
			auto start = std::chrono::system_clock::now();
			auto legacyStart = std::chrono::system_clock::to_time_t(start);
			ctime_s(tmBuff, sizeof(tmBuff), &legacyStart);
		}

		cout << ratten;
		cin >> eingabe;

		myfile << eingabe << ", ";

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
		myfile << "( "<< eingabe << " )" << endl << tmBuff << "Spieler - " 
			<< name << " / Punkte - " << punkte << endl;

		if (myfile.is_open())
		{
			myfile.close();
		}
		cout << "Die Zahl ist gleich " << eingabe << endl << endl;

		result();
		
		cout << "Noch einmal spielen (j/n)? ";

		string nochEine; cin >> nochEine;

		if (nochEine == "j")
		{
			continue;
		}
		else
		{
			break;
		}
	}
}