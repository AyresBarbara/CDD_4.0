package JavaPoo;

public class Carro {
	String modelo, cor;
	double preco;
	boolean ligado = false; 
	
	public Carro() {
		
	}
	public Carro(String m, String c) {
		this.modelo = m;
		this.cor = c;
	}
	
	public Carro(double p) {
		this.preco = p;
	}
	public Carro(String m, String c, double p) {
		this.modelo = m;
		this.cor = c;
		this.preco = p;
	}
	
	//Meus métodos
	public void ligar() {
		if(ligado = true) {
			System.out.println("O carro já está ligado");
		}else {
			System.out.println("Ligou");
			ligado = true;
		}
	}
	public void desligar() {
		if(ligado = false) {
			System.out.println("O carro já está desligado.");
		}else {
			System.out.println("Desligou");
		}
	}
	public void acelerar() {
		if(ligado = true) {
		System.out.println("Acelerou");
		}else {
			System.out.println("Primeiro ligue o carro");
		}
	}
	public void frear() {
		if(ligado = true) {
			System.out.println("Freou");
		}else {
			System.out.println(" Já está freado");
		}
		
	}

}
