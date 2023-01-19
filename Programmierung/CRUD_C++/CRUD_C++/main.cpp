#include <fstream>
#include <string>
#include <iostream>

int main()
{
	std::string myText;
	std::fstream newfile;

	std::string a;

	std::cin >> a;

	while (true)
	{
		if (a == "read")
		{
			newfile.open("tpoint.txt", std::ios::out);  // open a file to perform write operation using file object
			if (newfile.is_open()) //checking whether the file is open {
				newfile << "Tutorials point \n"; //inserting text
			newfile.close(); //close the file object
			}
		}
		if (a == "create")
		{
			std::cout << "Enter file name:";
			std::cin >> a;
			// Create and open a text file
			std::fstream MyFile("Text.txt");

			// Write to the file
			/*MyFile << "Files can be tricky, but it is fun enough!";*/

			// Close the file
			MyFile.close();
		}
		if (a == "write")
		{		
			std::cout << "Enter text:";
			std::string a;
			std::cin >> a;

			newfile.open("Text.txt", std::ios::out);  // open a file to perform write operation using file object
			if (newfile.is_open()) //checking whether the file is open {
				newfile << a; //inserting text
			newfile.close(); //close the file object
		}
	}
}