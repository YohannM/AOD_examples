#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define TAILLE_LISTE 100000000

typedef struct Element Element;
struct Element
{
    int nombre;
    Element *suivant;
};

void main() {
     
    clock_t start, end;
    double cpu_time_used;

    Element* tete_sans_localite_spatiale = malloc(sizeof(struct Element));

    Element* courant = tete_sans_localite_spatiale;
    for(int i = 0 ; i < TAILLE_LISTE; i++) {
        courant->nombre = i;
        courant->suivant =  malloc(sizeof(struct Element));
        courant = courant->suivant;
    }

    Element* tete_avec_localite_spatiale = malloc(sizeof(struct Element) * TAILLE_LISTE);

    courant = tete_avec_localite_spatiale;
    for(int i = 0 ; i < TAILLE_LISTE; i++) {
        courant->nombre = i;
        courant->suivant = courant + 1;
        courant = courant->suivant;
    }
    
    start = clock();

    courant = tete_sans_localite_spatiale;
    for(int i = 0 ; i < TAILLE_LISTE; i++) {
        int a = courant->nombre;
        courant = courant->suivant;
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("\nSans prendre en compte la localite spatiale : %f\n", cpu_time_used);

    start = clock();

    courant = tete_avec_localite_spatiale;
    for(int i = 0 ; i < TAILLE_LISTE; i++) {
        int a = courant->nombre;
        courant = courant->suivant;
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("\nEn prenant en compte la localite spatiale : %f\n", cpu_time_used);

}