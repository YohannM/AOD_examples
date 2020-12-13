#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define TAILLE_TAB 1000000000


void main() {
     
    clock_t start, end;
    double cpu_time_used;

    int* tab = malloc(TAILLE_TAB * sizeof(int));

    int somme = 0;

    for(int i = 0 ; i < TAILLE_TAB; i++) {
        tab[i] = 1;
    }
    
    start = clock();

    for(int n = 0; n < 3; n++) {
        for(int i = 0 ; i < TAILLE_TAB; i++) {
            somme += tab[i];
        }
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;


    printf("\nSans prendre en compte la localite temporelle : %f\n", cpu_time_used);

    somme = 0;

    start = clock();

    for(int i = 0 ; i < TAILLE_TAB; i++) {
        for(int n = 0 ; n < 3; n++) {
            somme += tab[i];
        }
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("\nEn prenant en compte la localite temporelle : %f\n", cpu_time_used);

    free(tab);

}