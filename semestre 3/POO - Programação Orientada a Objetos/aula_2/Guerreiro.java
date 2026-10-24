package aula_2;

public class Guerreiro extends Personagem {
    private int forca;
    private int armor;
    public Guerreiro (String nome, String classe, int total_HP, int current_HP, int level, int coins){
        super(nome, classe, total_HP);
        this.forca = 20;
        this.armor = 18;
    }
    public int getForca(){
        return forca;
    }
    public int getArmor(){
        return armor;
    }
    public void Atacar(){
        System.out.printf("Vcocê atacou o inimigo sua força é de %s", this.forca);
    }
}
