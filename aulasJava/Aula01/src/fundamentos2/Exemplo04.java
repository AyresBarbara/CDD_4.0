package fundamentos2;

public class Exemplo04 {

	public static void main(String[] args) {
		int arrayNum[]= {87, 68, 52, 5, 49, 83, 45, 12, 64};
		int total = 0;
		
		for(int i : arrayNum) //Sem chave pq só tem 1 linha de comando, vai rodar apenas 1 linha, o system já é fora do FOR
			
			total += i;
			System.out.printf("Soma dos elemntos arrayNum:%d\n ", total); 
	}

}
