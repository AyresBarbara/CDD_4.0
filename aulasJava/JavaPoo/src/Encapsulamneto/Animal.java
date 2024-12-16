package Encapsulamneto;

public class Animal {
	private String nome;
	private String tutor;
	private String rg;
	private String raca;
	private String dataNascimento;
	private int idade;
	
	public Animal() {
		
	}
	public Animal(String nome, String tutor, String rg, String raca, String data, int idade) {
		this.nome = nome;
		this.tutor = tutor;
		this.rg = rg;
		this.raca = raca;
		this.dataNascimento = data;
		this.idade = idade;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getTutor() {
		return tutor;
	}

	public void setTutor(String tutor) {
		this.tutor = tutor;
	}

	public String getRg() {
		return rg;
	}

	public void setRg(String rg) {
		this.rg = rg;
	}

	public String getRaca() {
		return raca;
	}

	public void setRaca(String raca) {
		this.raca = raca;
	}

	public String getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(String dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}
	

}
