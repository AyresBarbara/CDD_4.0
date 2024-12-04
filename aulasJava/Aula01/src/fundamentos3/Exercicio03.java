package fundamentos3;

import java.util.Scanner;
import java.util.StringTokenizer;

public class Exercicio03 {

	public static void main(String[] args) {
		Scanner leia = new Scanner(System.in);
		String texto;
		
		System.out.println("Digite seu texto:");
		texto = leia.nextLine();
		
		StringTokenizer exemplo = new StringTokenizer(texto);
		System.out.println(exemplo.countTokens());
		

	}

}
