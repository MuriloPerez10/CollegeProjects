/*
O programa que define uma estrutura Funcionário que tem como campos nome e salario. Vamos também criar uma função que recebe por referência uma estrutura do tipo Funcionário e reajusta o seu salário de acordo com a seguinte regra: salários menores que R$ 500,00 são reajustados em 12%; salários maiores ou iguais a R$ 500,00 são reajustados em 7%. Após a chamada da função os dados do funcionário são apresentados.
*/

#include <stdio.h>
#include <stdlib.h>
// definição da estrutura funcionário
struct Funcionario {
    char nome[80];
    float salario;
};
// definição da função reajustarSalario
// note que temos que colocar o operador * antes
// do nome do parametro, indicando que a passagem
// é por referência
void reajustarSalario (struct Funcionario *func) {  
    if (func->salario < 500) {
        // reajusta o salario em 12%
        func->salario = func->salario * 1.12;
    } 
    else {
        // reajusta o salario em 7%
        func->salario = func->salario * 1.07;
    } 
}
main () {
    // declaração da variável do tipo funcionario
    struct Funcionario f;
    // leitura dos dados do funcionário
    printf ("Nome: ");
    gets (f.nome);
    printf ("Salario: ");
    scanf ("%f", &f.salario);
    // chamada a função de reajuste de salario
    // note que temos que colocar o operador & antes do 
    // nome da variavel de estrutura, pois a estamos 
    // passando por referencia
    reajustarSalario (&f);
    // imprime os dados do funcionario
    printf ("%s - %.2f\n\n", f.nome, f.salario);
    system ("PAUSE");
}