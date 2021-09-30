#include <stdio.h> 
#include <stdlib.h>
#include <string.h> 
// definição da union 
union dados_aluno   {  
     char nome [40];   
     float nota;  
     int faltas; 
} ; 
main ( ) {   
     // declaração de uma variável da union    
     union dados_aluno NovoAluno; 
 
     printf ("\n Digite o nome do aluno="); 
     gets (NovoAluno.nome);  
     printf ("\n Nome do aluno="); 
     puts (NovoAluno.nome); 
     printf ("\n Digite a nota do aluno=");   
     scanf ("%f", &NovoAluno.nota); 
     printf ("\n Nota do aluno=%f", NovoAluno.nota); 
     printf ("\n Digite as faltas do aluno=");  
     scanf ("%d", &NovoAluno.faltas); 
     printf ("\n Faltas do aluno=%d", NovoAluno.faltas);  
     system ("PAUSE");
 }