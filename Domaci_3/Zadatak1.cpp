#include <iostream>
#include <HarmonicOscillator.h>



int main(){

    double time = 4.0;

    HarmonicOscillator oscilator(-10, 0, 2.5, 150, time);
    oscilator.write_file();

    return 0;
}