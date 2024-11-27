package fundamentos2;

import java.util.Scanner;

public class Exercicio02 {

	public static void main(String[] args) {
		Scanner lendo = new Scanner(System.in);
		int num, cont = 0;
		
		System.out.println("Digite o valor: ");
		num = lendo.nextInt();
		
		while (cont <= num) {
			
			if(cont %2 !=0) {
				System.out.println(cont);
			}
			cont++;
		}
	}

}
