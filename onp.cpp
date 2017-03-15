#include <iostream>
#include <string.h>
#include <locale>

using namespace std;

int main()
{
    string onp;
    getline(cin, onp);
    cout << "Podano: " << onp << endl;

    for (unsigned int i=0; i<onp.length(); i++)
        {
            if (onp[i] == ' ')
                ;
            else if (isdigit(onp[i]))
                cout << "liczba" << endl;
            else
                cout << "tekst" << endl;
        }


}
