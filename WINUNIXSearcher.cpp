#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <cstring>
#include "split.h"
#include "searcher.h"
#ifdef _WIN32
   //define  Windows 
   #define os "windows"
#elif __APPLE__
    #include "TargetConditionals.h"
    #if TARGET_IPHONE_SIMULATOR
         #define os "iphone_SIM"
    #elif TARGET_OS_IPHONE
        #define os "iphone"
    #elif TARGET_OS_MAC
        #define os "mac"
    #else
        #define os "mac"
    #endif
#elif __linux
    #define os "linux"
#elif __unix // all unices not caught above
    #define os "linux"
#endif


using namespace std;

unsigned int split(const string &txt, vector<string> &strs, char ch)
    {
        unsigned int pos = txt.find( ch );
        unsigned int initialPos = 0;
        strs.clear();
        while( pos != string::npos )
        {
            strs.push_back( txt.substr( initialPos, pos - initialPos + 1 ) );
            initialPos = pos + 1;
            pos = txt.find( ch, initialPos );
        }
        // Add the last one
        strs.push_back( txt.substr( initialPos, min( pos, txt.size() ) - initialPos + 1 ) );
        return strs.size();
    }


int search(vector<string> term, string sys)
{
    string searchcmd, searchcmdh;

    if (sys == "windows")
    {
        searchcmd = "dir %systemdrive%\\ /b /s";
        searchcmdh = "dir %systemdrive%\\ /s /a:h /b";

        for (int i=0; i<term.size();i++)
        {
            searchcmd = searchcmd + " | find /i \"" + term[ i ] + "\"";
            searchcmdh = searchcmdh + " | find /i \"" + term[ i ] + "\"";
        }
        const char * com = searchcmd.c_str();
        const char * com2 = searchcmdh.c_str();
        system(com);
        system(com2);
        return 0;

    }

    else if (sys == "linux")
    {

        searchcmdh = "ls / -a -R -q | cat";
        for (int i=0; i<term.size();i++)
        {
            searchcmdh = searchcmdh + " | grep -i '" + term[ i ] + "'";
        }
        const char * com2 = searchcmdh.c_str();
        system(com2);
        return 0;
    }

    else if (sys == "mac")
    {

        searchcmdh = "ls / -a -R | cat";
        for (int i=0; i<term.size();i++)
        {
            searchcmdh = searchcmdh + " | grep -i '" + term[ i ] + "'";
        }
        const char * com2 = searchcmdh.c_str();
        system(com2);
        return 0;
    }

    else;
    {
        return 1;
    }

}


int main(int argc, char** argv)
{
    string sys = os;
    string prein;
    if ( argc == 1 )
    {
        cout << "This tool is made by Xavier G. Wrenn.\n";
        cout << "For reference, use " << argv[ 0 ] << " [full search]\n";
        cout << "Search term:";
        getline( cin, prein, '\n' );
    }

    else if ( argc >= 2 )
    {
        string up;
        for (int i = 1; i < argc; i++)
        {
            if ( i == 1)
            {
                up = argv[ i ];
                prein = up;
            }
            else
            {
                up = argv[ i ];
                prein = prein + " " + up;
            }
        }
        //cout << endl << prein << endl;
    }

    vector<string> searchq;
    split( prein, searchq, ' ');
    search(searchq, sys);
}
