/*
 * sztos.cpp
 */


#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

void push(int stos[], int &sp, int dane)
{
    cout << dane << " ";
    stos[sp] = dane;
    sp++;
}
int pop(int stos[], int &sp)
{
    sp--;
    return stos[sp];
}

int main()
{

    int *stack; // wskaźniczek sztosika
    int sr; // rozmiar sztosika
    int sp = 0; // stack pointer

    cout << "Podaj rozmiar: ";
    cin >> sr;
    if (!cin)
        {
            cout << "Błędne dane!";
            return -1;
        }
    stack = new int[sr];

    srand(time(NULL));

    for (int i=0; i<sr; i++)
        push(stack, sp, rand()%100 + 1); // wstaw sztosik

    cout << endl;

    for (int i=0; i<sr; i++)
        cout<< pop(stack, sp) << " "; // zdejmij sztosik

	return 0;
}

