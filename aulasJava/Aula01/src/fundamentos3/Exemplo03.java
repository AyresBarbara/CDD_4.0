package fundamentos3;

public class Exemplo03 {

	public static void main(String[] args) {
		String str = "Hello World";
		String s1 = "Hello";
		String s2 = "HELLO";
		
		//imprimie a partir da 6º posição
		String resultado = str.substring(6);
		System.out.println(resultado);
		
		//imprime a partir da posição indicada, até o final da palavra
		String resultado1 = str.substring(3,8);
		System.out.println(resultado1);
		
		//Maiúsculo
		String resultado2 = str.toUpperCase();
		System.out.println(resultado2);
		
		//Minusculo
		String resultado3 = str.toLowerCase();
		System.out.println(resultado3);
		
		//Trim - retira os espaços em branco no inicio e no fim
		String resultado4 = str.trim();
		System.out.println(resultado4);
		
		//Pega o caracter na posição indicada
		char c = str.charAt(1);
		System.out.println(c);
		
		//Comparando Strings
		boolean b1 = s1.equals("Hello");
		boolean b2 = s1.equals(s2);
		boolean b3 = s1.equalsIgnoreCase(s2);
		boolean b4 = s1.equalsIgnoreCase("azul");
		System.out.println(b1);
		System.out.println(b2);
		System.out.println(b3);
		System.out.println(b4);
		
		//Conta o tamanho da string
		int tam = str.length();
		System.out.println(tam);
		
		int pos = str.indexOf("l");
		System.out.println(pos);
		
		int pos2 = str.lastIndexOf("l");
		System.out.println(pos2);
		
	}

}
