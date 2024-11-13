package aula1;

public class Exemplo03 {

	public static void main(String[] args) {
		int a = 3;
		int b = 4;
		int c = 7;
		System.out.println((a+b)/c);
		System.out.println(!((a>b) &&(a<c)));
		
		System.out.println(a % 2 == 0 ? ++a: a++); // Se o resto da divisão de A por 2, for 0, execute ++a, se não a++
		
		if(a++ >= b) // 3>=4 - primeiro imprime A, depois ele atribui o ++
			System.out.println(--c); // Por ter só uma linha de código, não precisa abrir {}(é um constante)
		
		else 
				System.out.println(c++);
	}

}
