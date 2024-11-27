package fundamentos2;

public class Exercicio07 {
	public static void main(String[] args) {
		int multTres= 0, multCinco = 0, soma =0;
		
		for(int x = 1; x <= 20; x++) {
			if(x %3 ==0) {
				multTres += x;
			}
			if(x %5 == 0) {
				multCinco += x;
			}
		}
		soma = multTres + multCinco;
		System.out.println("A soma dos Múltiplos de 3 é "+ multTres +" e a soma dos múltiplos de 5 é "+ multCinco +", a soma total é " + soma);
	}

}
