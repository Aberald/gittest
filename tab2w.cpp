/*
 * TAB2W.cpp
 *
 *
 */


#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

int tab2w()
    {
        int w, k, i, j;

        srand(time(NULL));

        cout << "Podaj wiersze i kolumny: ";
        cin >> w >> k;

        int **tab; // wskaźnik wskaźnika
        try
            {
                tab = new int *[w];
            } catch(bad_alloc) {
                cout << "Za mało pamięci";
                return -1;
            }
        for (i=0; i<w; i++)
            {
               try{
                tab[i] = new int [k];
                } catch(bad_alloc) {
                cout << "Za mało pamięci";
                return -1; }
            }
        for (i=0; i<w; i++)
            {
                for (j=0; j<k; j++)
                    {
                        tab[i][j] = rand()%100 + 1;
                        cout << setw(4) << tab[i][j];
                    }
                cout << "\n";
            }
        for (i=0; i<w; i++)
            delete [] tab[i];

        delete [] tab;

        return 0;
    }

int main()
    {
        tab2w();
        return 0;
    }


