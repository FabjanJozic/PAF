#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>

#include <HarmonicOscillator.h>

using namespace std;


void HarmonicOscillator::move(){
    A.push_back(-(_K/_m)*X.back());
    V.push_back(V.back()+A.back()*dt);
    X.push_back(X.back()+V.back()*dt);
}


double HarmonicOscillator::write_file(){
    for(int i; i < T.size(); i++){
        move();
    }
    X.pop_back();
    V.pop_back();
    A.pop_back();
    ofstream ofs("oscilator.txt", ofstream::out);
    if(ofs.is_open()){
        for(auto & x : X){
            for(auto & v : V){
                for(auto & a : A){
                    for(auto & t : T){
                        ofs << x <<"-o-"<< v <<"-o-"<< a <<"-o-"<< t <<endl;
                    }
                }
            }
        }
    }else{
        cout<<"Pogreška pri ispisu dokumenta."<<endl;
    }
    return 0;
}


HarmonicOscillator::HarmonicOscillator(double x0, double v0, double K, double m, double time){
    _x0 = x0;
    _v0 = v0;
    _K = K;
    _m = m;
    _time = time;
    A.push_back(-(_K/_m)*_x0);
    V.push_back(_v0);
    X.push_back(_x0);
    T.push_back(0.0);
    while(T.back() <= _time){
        T.push_back(T.back()+dt);
    }
}
