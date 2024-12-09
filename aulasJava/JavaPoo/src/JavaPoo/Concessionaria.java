package JavaPoo;

public class Concessionaria {

	public static void main(String[] args) {
		Carro c1 = new Carro();
		Carro c2 = new Carro();
		Carro c3 = new Carro();
		Carro c4 = new Carro();
		
		
		c1.modelo = "Fiat UNO";
		System.out.println(c1.modelo);
		
		c1.cor = "preto";
		c2.preco = 14.500;
		
		c1.acelerar();
		c1.ligar();
		c1.desligar();
		
		
	}

}
