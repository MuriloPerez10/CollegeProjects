int main()
{
    int i,n,l,p,escolha;
    //botao power da aplicação
    while(p!=1){
        printf("Digite qual programa escolhe roda 1/NumerosPares 2/NumerosImpares");
        scanf("%d",&escolha);
    switch(escolha){
        //nesse caso voce entra na função de numeros pares
    case 1:    
        printf("Digite quantos numeros Pares:");
        scanf("%d",&n);
    
    for(i=1;i<=n;i+2){
        printf("%d ",i); } break;
    
        //nesse caso voce entra na função de numeros impares
    case 2:
        printf("Digite quantos numeros impares");
        scanf("%d",&n);
    
    for(i=0;i<=n;i+2){
        printf("%d ",i); } break;
        
    }
    printf("deseja continuar com o programa? 1/sair 0/continuar");
    scanf("%d",&p);
    }
    printf("\n adeus");
    return 0;
}