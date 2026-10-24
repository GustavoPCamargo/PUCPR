package aula_2;

public class Arqueiro extends Personagem {
    private int quantidade_flechas;
    private int precisao;
    public Arqueiro (String nome, String classe, int total_HP, int current_HP, int level, int coins){
        super(nome, classe, total_HP);
        this.quantidade_flechas = 20;
        this.precisao = 20;
    }

    public void Atirar(){
        if (this.quantidade_flechas > 0){
            System.out.printf("Você atirou uma felcha com sucesso :D, vc tem %d flechas sobrando", this.quantidade_flechas);
        } else {
            System.err.println("Você não tem mais flechas sobrando");
        }
    }
}
