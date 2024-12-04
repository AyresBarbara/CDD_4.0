package fundamentos3;

import java.util.StringTokenizer;

public class Exemplo04 {

	public static void main(String[] args) {
		String valor = "CDD4.0 - Java";
		
		//Comparando strings e ignorando CamelCase
		System.out.println(valor.compareTo("CDD4.0 - Java") == 0? true: false);
		System.out.println(valor.compareTo("CDD4.0 - JAVA") == 0? true: false);
		System.out.println(valor.compareToIgnoreCase("CDD4.0 - JAVA") == 0? true: false);
		
		//Verifica se o valor começa com o valor especificado
		System.out.println(valor.endsWith("Java"));
		System.out.println(valor.startsWith("C"));
		System.out.println(valor.startsWith("DD", 1));
		
		//Divide a String em partes, separadas por espaço em branco
		StringTokenizer  exemplo = new StringTokenizer("O mundo não é mais o mesmo, mas não iremos desistir nunca");
		System.out.println(exemplo.countTokens());
		
	}

}
