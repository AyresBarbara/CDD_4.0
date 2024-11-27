package fundamentos2;

import java.util.Scanner;

public class Exercicio06 {

	public static void main(String[] args) {
		Scanner lendo = new Scanner(System.in);
		double nota=0, media;
		int qtdAlunos;

		System.out.println("Quantos alunos?");
		qtdAlunos = lendo.nextInt();
		
		for( int i = 0; i < qtdAlunos; i++) {
			System.out.printf("Digite a nota do %d ª aluno: ", i+1);
			nota += lendo.nextDouble();
			
		}
		media = nota / qtdAlunos;
		System.out.printf("A média dos alunos é %.2f", media);
				
	}

}
