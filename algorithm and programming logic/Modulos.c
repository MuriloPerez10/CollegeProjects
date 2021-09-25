#include <stdio.h>
#include <stdlib.h>

int a,b,c,r,total;

//funçao para realizar a adiçao
int Adicao(){
    r = a+b;
    return(r);
}

//procedimento para entrada de dados
void dado(){
    printf("\n escreva um numero: ");
    scanf("%d",&a);
    printf("\n escreva um numero: ");
    scanf("%d",&b);
}

//programa para interação com o usuario
int main()
{
    printf("quer calcular? (0)sim  (1)nao");
    scanf("%d",&c);
    if(c == 0){
        dado(); //procedimento entrada
        total = Adicao(); //funçao puxada
        printf("total-> (%d)",total);
    }else{
        printf("ate a proxima");
    };
    return 0;
}
