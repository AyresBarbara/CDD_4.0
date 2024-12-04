package fundamentos3;

import java.util.Scanner;

public class Exercicio05 {

	public static void main(String[] args) {
		Scanner leia = new Scanner(System.in);
		String texto ;
		
		System.out.println("Digite seu texto:");
		texto = leia.nextLine();
		System.out.println(texto.toUpperCase());
	}

}
