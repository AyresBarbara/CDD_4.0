package Heranca;

public class Professor extends Pessoa {
	double salario;
	
	public Professor(String nome, String cpf, String telefone) {
		super(nome, cpf, telefone);
	}
	public void AplicarProva() {
		System.out.println("Aplicando prova!!");
	}
	public void Certificar() {
		System.out.println("Certificado!");
	}
	

}
