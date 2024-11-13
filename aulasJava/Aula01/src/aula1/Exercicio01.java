package aula1;

import java.util.Scanner;

public class Exercicio01 {

	public static void main(String[] args) {
		Scanner leia = new Scanner(System.in);
		
		System.out.println("Digite um valor: ");
		int valor = leia.nextInt();
		
		if(valor >0) {
			System.out.println("O valor é positivo!");
		} else {
			System.out.println("O valor é negativo!");
		}
	}

}
