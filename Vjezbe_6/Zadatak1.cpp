#include <iostream>
#include <cmath>

using namespace std;

void pravac(double Ax, double Ay, double Bx, double By) {
    double k;
    k = (By -Ay)/(Bx - Ax);
    double f;
    f = -k*Ax + Ay;
    if(f < 0){
        cout<<"Jednadžba pravca je  y="<< k <<"x"<< f <<endl;
    } else if(f > 0){
        cout<<"Jednadžba pravca je  y="<< k <<"x+"<< f <<endl;
    } else{
        cout<<"Jednadžba pravca je  y="<< k <<"x"<<endl;
    }
}

int main() {

    pravac(4.0, 2.0, 3.0, 4.0);

    return 0;
}