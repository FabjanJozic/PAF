#include <Particle.h>
#include <iostream>
#include <cmath>

using namespace std;

void Particle::move(){

    vx += 0.;
    vy += g*dt;
    x += vx*dt;
    y += vy+dt;
    t += dt;

}

double Particle::range(){
    while(y >= 0){
    move();
    }
    cout << x <<endl;
    return x;
}

double Particle::time(){
    while(y >= 0){
    move();
    }
    cout << t <<endl;
    return t;
}





Particle::Particle(double v0, double alpha, double x0, double y0, double step){

    t = 0;
    vx = v0*cos(alpha);
    vy = v0*sin(alpha);
    x = x0;
    y = y0;

}

