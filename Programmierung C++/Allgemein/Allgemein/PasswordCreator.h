#pragma once
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

class PasswordCreator
{
public:
	string CreatePassword() {


		string logo = " ----------------------\n | Passwort-Ersteller |\n ----------------------\n\n";
		cout << logo;
		cout << "Wie lang soll das Passwort sein? ";
		int length; cin >> length;
		string password = "";
		int r;
		string savePassword;

		for (size_t i = 0; i < length; i++)
		{
			r = 33 + (rand() % 93);
			password += char(r);
		}

		cout << "Wenn Sie Ihr Passwort speichern m�chten - 'j' SONST 'n'";
		cin >> savePassword;

		if (savePassword == "j")
		{
			string name;
			cout << "das Passwort nennen: ";
			cin >> name;

			ofstream myfile;
			myfile.open("passwords.txt", fstream::app);
			string output = name + " - " + password + "\n";

			if (myfile.is_open())
			{
				myfile << output;
				myfile.close();

				cout << "Sie haben Ihr Passwort erfolgreich gespeichert\n";
			}
			else cout << "Datei kann nicht ge�ffnet werden";
		}

		return password;
	}
};

