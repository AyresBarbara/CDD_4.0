package JavaPoo;

public class TesteCalculadora {

	public static void main(String[] args) {
		Calculadora calculadora = new Calculadora();
		//SOMAR
		double resp = calculadora.somar(5, 8, 10);
		System.out.println(resp);
		
		resp = calculadora.somar(5, 8);
		System.out.println(resp);
		
		//SUBTRAIR
		resp = calculadora.subtrair(15, 10);
		System.out.println(resp);
		
		resp = calculadora.subtrair(20, 10, 5);
		System.out.println(resp);
		
		//MULTIPLICAR
		resp = calculadora.multiplicar(5, 3);
		System.out.println(resp);
		
		resp = calculadora.multiplicar(5, 3, 2);
		System.out.println(resp);
		
		//DIVIDIR
		resp = calculadora.dividir(20, 5);
		System.out.println(resp);

		resp = calculadora.dividir(20, 5, 2);
		System.out.println(resp);
	}

}
