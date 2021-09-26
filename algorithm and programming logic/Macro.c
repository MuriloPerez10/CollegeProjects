/*
 O programa cria uma macro para calcular a área de uma circunferência. Posteriormente, essa macro é chamada na função main().
*/

#include <stdio.h> 
#include <stdlib.h>
// definição da constante simbolica PI 
#define PI 3.1415 
// definição da macro
#define AREA(r) (PI * r * r) 
main() {   
    float raio;   
    printf ("Raio: ");   
    scanf ("%f", &raio);   
    // chamada a macro    
    float area = AREA(raio);   
    printf ("Area = %.2f\n", area);  
    system ("PAUSE"); 
}