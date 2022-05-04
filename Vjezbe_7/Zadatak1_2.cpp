#include <iostream>
#include <Particle.h>


int main() {

    Particle part1(10, 0.3, 0, 0);
    part1.range();
    part1.time();

    Particle part2(20, 0.3, 0, 0);
    part2.range();
    part2.time();

    Particle part3(10, 0.5, 0, 0);
    part3.range();
    part3.time();

    return 0;

}