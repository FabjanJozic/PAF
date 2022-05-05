#include <cmath>


class Particle {

    private:
    double vx, vy, x, y, t;
    double dt;
    double g = -9.81;

    void move();


    public:

    Particle(double v0, double alpha, double x0, double y0, double step = 0.001);

    double range();
    double time();

};
