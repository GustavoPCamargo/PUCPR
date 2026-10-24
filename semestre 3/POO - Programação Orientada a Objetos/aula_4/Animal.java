package aula_4;

class Animal {
    protected String nome;
    protected String raca;
    protected String cor;
    protected int idade;
    protected String classe; 
    
    public void comer() {
    System.out.println("Nhami");
    }
}

public class Main {
    public static void main(String[] args) {
        Gato g = new Gato();
        g.comer();

        Passaro p = new Passaro();
        p.comer();
    }
}