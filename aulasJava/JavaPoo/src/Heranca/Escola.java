package Heranca;

public class Escola {

	public static void main(String[] args) {
		Aluno a1 =  new Aluno("Bárbara", "01547899652", "08198525565");
		Professor p1 = new Professor("Wellington", "4156789123485", "448454494765");
		
		a1.sofrer();
		p1.AplicarProva();
		
		System.out.println(a1.nome +"\n"+ a1.cpf+"\n"+ a1.telefone);

	}

}
