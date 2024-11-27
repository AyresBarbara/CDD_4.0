package fundamentos2;

import java.util.Scanner;

public class Exercicio01 {

	public static void main(String[] args) {
		Scanner leia = new Scanner(System.in);
		int qtdAlunos, cont=0;
		double nota=0, media;
		
		System.out.println("Digite quantos alunos tem na sala: ");
		qtdAlunos = leia.nextInt();
		
		while(cont < qtdAlunos) {
			System.out.printf("Qual a nota do %dª aluno? \n", cont+1);
			nota += leia.nextDouble();
			cont ++;
		}
		media = nota/ qtdAlunos;
		System.out.printf("A média da turma é %.2f \n", media);
		System.out.println("Fim de execução!");

	}

}
