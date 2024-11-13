package aula1;

import java.util.Scanner;

public class Exemplo05 {

	public static void main(String[] args) {
		Scanner leia = new Scanner(System.in);
		
		System.out.println("Digite seu número: ");
		double resp = leia.nextDouble();
		System.out.println("O número foi " + resp);
	}

}
