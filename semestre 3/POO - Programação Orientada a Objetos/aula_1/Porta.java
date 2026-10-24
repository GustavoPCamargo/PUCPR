package aula_1;

public class Porta {

    public String cor;
    public String material;
    public float tamanho;
    public boolean taaberto;
    public String modelo;

    public void abrir() {
        System.out.println("Vc abriu a porta");
    }

    public void fechar(){
        System.out.println("Vc fechou a porta");
    }

    public void trancar(){
        System.out.println("Vc trancou a porta");
    }

    public static void main(String[] args) {
        Porta porta = new Porta();

        porta.abrir();
        porta.fechar();
        porta.trancar();
    }
}
