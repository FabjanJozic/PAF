#include <Particle.h>
#include <iostream>
#include <cmath>

using namespace std;


Particle::Particle(double v0, double alpha, double x0, double y0, double step){

    t = 0;
    vx = v0*cos(alpha);
    vy = v0*sin(alpha);
    x = x0;
    y = y0;
    dt = step;

}


void Particle::move(){
    while(y >= 0){
    vx += 0.;
    vy += g*dt;
    x += vx*dt;
    y += vy+dt;
    t += dt;
    }
}

double Particle::range(){
    move();
    cout << x <<endl;
    return x;
}

double Particle::time(){
    move();
    cout << t <<endl;
    return t;
}




