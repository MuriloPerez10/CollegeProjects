include <stdio.h>

int main()
{
    int str[1][1],x,y,n,i;
    //arrumar contador
    //leitura de valores
    x = 0;
    for(x = 0;x<=1; x++ ){
        y = 0;
        printf("teste");
        for(y = 0 ; y<=1 ;y++){
            n = 0;
            printf("\n digite um numero: ");
            scanf("%d",&n);
        str[x][y] = n;
        };
    };
    printf("%d ",str[0][0]);
    printf("%d ",str[0][1]);
    printf("%d ",str[1][0]);
    printf("%d ",str[1][1]);
    //demonstrações de valores armazenados
    /*for(x = 0;x<=1;x++){
        printf("numeros digitados na linha %d -> ",x);
        for(y = 0;y<=1;y++){
            printf(" %d ",str[x][y]);
        };
    };*/
    printf("\n fim do programa");
}