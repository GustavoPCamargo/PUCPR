package aula_1;

public class Pistola {
    
    public String modelo;
    public String cor;
    public int munição;
    public float tamanho;
    public int numero_de_serie;

    public void atirar(){
        System.out.printf("vc deu um disparo agora vc tem %d de munição", munição);
    }

    public void recarregar(){
        System.out.printf("vc recarregou a arma, agora vc tem %d de munição", munição);
    }

    public void mirar(){
        System.out.println("a partir de agora vc esta mirando e tem mais precisão");
    }

    public static void main(String[] args) {

        Pistola pistola = new Pistola();

        pistola.munição = 12;
        pistola.atirar();
        pistola.munição -= 1;
        pistola.recarregar();
        pistola.mirar();

    }
}
