#include <iostream>
#include <cmath>

using namespace std;

void tocka_i_kruznica(double Ax, double Ay, double Sx, double Sy, double r){
    double udaljenost;
    if(r > 0){
        udaljenost = sqrt(pow((Ax - Sx), 2) + pow((Ay - Sy), 2));
    } else{
        cout<<"Pogreška pri unosu vrijednosti radijusa. Radijus mora biti pozitivan broj."<<endl;
    }
    if(udaljenost < r){
        cout<<"Točka se nalazi unutar kružnice."<<endl; 
    }else if(udaljenost == r){
        cout<<"Točka se nalazi na kružnici."<<endl;
    }else{
        cout<<"Točka se nalazi izvan kružnice."<<endl;
    }
}


int main(){

    tocka_i_kruznica(2, 2, 1, 1, 2);

    return 0;

}