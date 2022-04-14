#include <iostream>
#include <cmath>

using namespace std;



void interval(int lista[], int prvi, int zadnji){
    for(int i = prvi; i <= zadnji; i++){
        cout<< lista[i] <<" ";
    }
    cout<<endl;
}

void okretanje(int lista[], int velicina){
    for(int i = velicina; i >= 0; i--){
        cout<< lista[i] <<" ";
    }
    cout<<endl;
}


void zamjena(int lista[], int velicina, int prvi, int drugi){
    int prvi_z, drugi_z;
    prvi_z = lista[prvi];
    drugi_z = lista[drugi];
    lista[prvi] = drugi_z;
    lista[drugi] = prvi_z;
    for(int i = 0; i <= velicina; i++){
        cout<< lista[i] <<" ";
    }
    cout<<endl;
}


void sortiranje(int lista[], int velicina, char nacin){
    if(nacin == '>'){
        for(int a = 0; a <= velicina; a++){
            for(int b = 0; b <= velicina; b++){
                if(lista[a] > lista[b]){
                    int usporedni = lista[a];
                    lista[a] = lista[b];
                    lista[b] = usporedni;
                }
            }
        }
    } else if(nacin == '<'){
        for(int c = 0; c <= velicina; c++){
            for(int d = 0; d <= velicina; d++){
                if(lista[c] < lista[d]){
                    int usporedni = lista[c];
                    lista[c] = lista[d];
                    lista[d] = usporedni;
                }
            }
        }
    } else{
        cout<<"\nPogreška pri upisu mogućnosti sortiranja niza.\nUpišite < ili >.\n"<<endl;
    }
    for(int i = 0; i <= velicina; i++){
        cout<< lista[i] <<" ";
    }
    cout<<endl;
}




int main(){

    int polje[7] = {1,2,5,6,12,4,7};

    //interval(polje, 1, 3);

    //okretanje(polje, 6);

    //zamjena(polje, 6, 0, 2);

    //sortiranje(polje, 6, '<');

    return 0;
}