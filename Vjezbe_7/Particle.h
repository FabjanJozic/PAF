#include <cmath>


class Particle {

    private:
    double vx, vy, x, y, t;
    double dt;
    double g = -9.81;

    /*
    Particle(double v0, double alpha, double x0, double y0, double step = 0.001){
        vx = v0*cos(alpha);
        vy = v0*sin(alpha);
        x = x0;
        y = y0;
        dt = step;
    } */

    void move();


    public:

    Particle(double v0, double alpha, double x0, double y0, double step = 0.001);

    double range();
    double time();

};
