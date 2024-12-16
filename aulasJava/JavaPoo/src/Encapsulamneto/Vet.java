package Encapsulamneto;

public class Vet {

	public static void main(String[] args) {
		Animal a1 = new Animal();
		
	a1.setNome("Totó");
	a1.setIdade(2);
	a1.setRaca("Vira-Lata");
	a1.setTutor("Junior");
	a1.setRg("5959562");
	
	System.out.println("*--------------------------------------*");
	System.out.println("Nome do Pet: "+ a1.getNome());
	System.out.println("Idade: "+ a1.getIdade());
	System.out.println("Nome do tutor: " + a1.getTutor());
	System.out.println("Rg Tutor: " + a1.getRg());
	System.out.println("Raça do Animal: " + a1.getRaca());
	System.out.println("*---------------------------------------*");
		
		

	}

}
