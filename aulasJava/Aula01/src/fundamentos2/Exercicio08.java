package fundamentos2;

import java.util.Scanner;

public class Exercicio08 {

	public static void main(String[] args) {
		Scanner lendo = new Scanner(System.in);
		int tamanho= 4;
		int arrayA[] = new int [tamanho];
		int arrayB[] = new int [tamanho];
		int arrayC[] = new int [tamanho];
		int arrayD[] = new int [tamanho];
		
		for(int i =0; i < tamanho; i++){
			System.out.println("Digite o valor do Array A: ");
			arrayA[i] = lendo.nextInt();
		}

		for(int i =0; i < tamanho; i++){
			System.out.println("Digite o valor do Array B: ");
			arrayB[i] = lendo.nextInt();
		}
		for(int i =0; i < tamanho; i++){
			System.out.println("Digite o valor do Array C: ");
			arrayC[i] = lendo.nextInt();
		}
		for(int i =0; i < tamanho; i++){
			System.out.println("Digite o valor do Array D: ");
			arrayD[i] = lendo.nextInt();
		}
		for(int i : arrayA) {
			System.out.print(i +" ");
		}
		System.out.println();
		for(int i : arrayB) {
			System.out.print(i +" ");
		}
		System.out.println();
		for(int i : arrayC) {
			System.out.print(i +" ");
		}
		System.out.println();
		for(int i : arrayD) {
			System.out.print(i +" ");
		}
}
}
