#include <iostream>
#include <random>
#include <string>
#include <fstream>

using namespace std;

int random_number(int x, int y)
{
	std::random_device dev;
	std::mt19937 rng(dev());
	std::uniform_int_distribution<std::mt19937::result_type> dist6(x, y); // distribution in range [1, 6]

	return dist6(rng);
}

void result()
{
    ifstream myfile("zahlenraten_resultatent.txt");
    string line, buffer[3];
    const size_t size = sizeof buffer / sizeof * buffer;
    size_t i = 0;
    /*
     * Read all lines of file, putting them into
     * a circular buffer of strings.
     */
    while (getline(myfile, line))
    {
        buffer[i] = line;
        if (++i >= size)
        {
            i = 0;
        }
    }
    /*
     * Print the lines.
     */
    for (size_t j = 0; j < size; ++j)
    {
        cout << buffer[i] << "\n";
        if (++i >= size)
        {
            i = 0;
        }
    }
}