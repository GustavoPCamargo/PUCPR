package aula_2;

public class Mago extends Personagem {
    private int mana;
    private int poder_magico;
    public Mago (String nome, String classe, int total_HP, int current_HP, int level, int coins){
        super(nome, classe, total_HP);
        this.mana = 67;
        this.poder_magico = 20;
    }
    public void LancarMagia(){
        if (this.mana >= 10){
            System.out.printf("Você laçou a magia :D, vc tem %d mana sobrando", this.mana);
            this.mana -= 10;
        } else {
            System.out.printf("Você tem %d mana e precisa de no minimo 10 pra lançar a magia ;-;", this.mana);
        }
    }
}
