#include <stdio.h>
#include <math.h>

int main(void){

    double x1, x2, y1, y2, distancia;

    scanf(" %lf %lf", &x1, &y1);
    scanf(" %lf %lf", &x2, &y2);

    distancia = sqrt((x1-x2)*(x1-x2) + (y2-y1)*(y2-y1));

    printf("%.4f\n", distancia);

    return 0;
}
