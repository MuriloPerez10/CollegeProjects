int main()
{
    //transformador de numeros binario
    int i,j,d,n,resto[64];
    printf("escreva um numero");
    scanf("%d",&n);
    d = n;
    i = 0;
    //calculo de divisão para transfomção em binario
    while (d>=2){
        resto[i] =  d % 2;
        d = d / 2;
        i++;
    }
    resto[i] = d;
    printf("\n \n %d decimal em binario = ",n);
    
    //mostrando os codigo binarios na ordem correta
    //OBS: numeros binarios se le da direita para a esquerda
    for (j=i;j>=0;j--) {
        printf("%d ",resto[j]);
    }
    //finalização do programa
    printf("\n fim");
    system("pause");
    
    return 0;
}
