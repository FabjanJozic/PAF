#include <iostream>
#include <cmath>
#include <vector>

using namespace std;


class HarmonicOscillator {

    private:

    double x, v;
    double dt = 0.001;
    
    vector<double> X;
    vector<double> V;
    vector<double> A;
    vector<double> T;

    void move() ;


    public:

    HarmonicOscillator(double x0, double v0, double K, double m, double time);

    double _x0, _v0;
    double _K, _m;
    double _time;

    double write_file();

};