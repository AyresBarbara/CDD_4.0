package fundamentos3;

public class Exemplo03 {

	public static void main(String[] args) {
		String str = "Hello World";
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
	}

}
