package fundamentos3;

public class Exercicio06 {

	public static void main(String[] args) {
		String arrayString[] = {"a", "vida", "é", "bela"};
		int tam = arrayString.length;
		
		for(int i =0; i< tam; i ++)
		System.out.print(arrayString[i].toUpperCase() + " ");
	}

}
