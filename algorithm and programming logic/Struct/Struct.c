/*
Um aluno possui um código (inteiro), um nome e três notas. O seguinte programa lê os dados de um aluno, apresenta-os na tela juntamente com a média aritmética de suas notas.
*/


#include <stdio.h> 
#include <stdlib.h>
#include <string.h>
// definição da estrutura aluno
struct Aluno {  
     int codigo;  
     // o nome é representado por uma string 
     char nome[80];  
     // as notas são armazenadas em um vetor
     float notas[3];
}; 
 
main () { 
     // declaração da variável da estrutura Aluno
     struct Aluno umAluno; 
     // leitura do código
     printf ("Codigo: ");
     scanf ("%d", &umAluno.codigo);  
     getchar(); 
     // leitura do nome. Usamos o comando gets() para ler a string 
     printf ("Nome: ");  
     gets (umAluno.nome);  
     // leitura das notas do aluno. Percorremos o vetor com um for   
     int i; 
     for (i = 0; i < 3; i++) {    
            printf ("Nota %d: ", i + 1); 
            scanf ("%f", &umAluno.notas[i]); 
     }  
     float soma = 0;  
     // calculo da media do aluno
     for (i = 0; i < 3; i++) { 
            soma += umAluno.notas[i];  
     }  
     printf ("\n*** Dados do Aluno ***\n"); 
     printf ("Codigo: %d\n", umAluno.codigo);  
     printf ("Nome: ");  
     puts (umAluno.nome);
     printf ("Notas: %.1f %.1f %.1f\n", umAluno.notas[0], umAluno.notas[1], umAluno.notas[2]);   
     printf ("Media: %.1f\n\n", soma / 3); 
     system ("PAUSE");
}