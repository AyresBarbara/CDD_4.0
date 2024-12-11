package Heranca;

public class Funcionario extends Pessoa{
	double salario;
	
	public Funcionario(String nome, String cpf, String telefone, double salario) {
		super(nome, cpf, telefone);
	}

	public void dever() {
		System.out.println("Tô liso!! Eu tô liso");
	}
	public void receber() {
		System.out.println("Glória Deus");
	}
}
