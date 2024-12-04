package fundamentos3;

public class Exercicio07 {

	public static void main(String[] args) {
		String arrayString[] = {"a", "vida", "é", "bela"};
		int tam = arrayString.length;
		
		for(int i = tam-1; i >= 0; i--)
		System.out.print(arrayString[i] + " ");

	}

}
