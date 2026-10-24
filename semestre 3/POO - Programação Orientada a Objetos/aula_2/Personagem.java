package aula_2;
import java.util.Scanner;
import java.util.Random;

public class Personagem {
    Random random = new Random();


    private String name;
    private String classe;
    private int total_HP;
    private int current_HP;
    private int level;
    private int coins;

    public Personagem(String name, String classe, int total_HP){
        this.name = name;
        this.classe = classe;
        this.total_HP = total_HP;
        this.level = 1;
        this.coins = 100;
        this.current_HP = total_HP;
    }

    public String getName(){
        return name;
    }

    public String getClasse(){
        return classe;
    }

    public int getTotal_HP(){
        return total_HP;
    }

    public int getCurrent_HP(){
        return current_HP;
    }

    public int getLevel(){
        return level;
    }

    public int getCoins(){
        return coins;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setClasse(String classe){
        this.classe = classe;
    }

    public void Receber_Dano(){
        int dano = random.nextInt(20) + 1;

        if (this.current_HP - dano >= 0){
            this.current_HP -= dano;
        } else {
            current_HP = 0;
        }
    }

    public void Recuperar_Vida(){
        int valor = random.nextInt(20) + 1;

        if (this.current_HP + valor <= this.total_HP){
            this.current_HP += valor;
        } else {
            this.current_HP = this.total_HP;
        }
    }

    public void Subir_Nivel(){
        this.level += 1;
    }

    public void Receber_Moedas(int quantidade){
        if (quantidade > 0){
            this.coins += quantidade;
        }
    }

    public void Gastar_Moedas(int quantidade){
        if (quantidade > 0 && quantidade <= this.coins){
            this.coins -= quantidade;
        }
    }


    public static void main(String[] args) {


        Personagem g = new Guerreiro(Baltazar);












        /*Personagem personagem = new Personagem("------", "-----", 90);

        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha um nome pro seu personagem: ");
        String nome = scanner.nextLine();
        personagem.setName(nome);

        System.out.println("Escolha uma classe pro seu personagem: ");
        String classe = scanner.nextLine();
        personagem.setClasse(classe);

        System.out.printf("Você é %s vc é um %s em busca da verdade por tras da morte de seu pai.%n", personagem.getName(), personagem.getClasse());
        System.out.printf("Nome: %s%n", personagem.getName());
        System.out.printf("Classe: %s%n", personagem.getClasse());
        System.out.printf("Vida: %d/%d%n", personagem.getCurrent_HP(), personagem.getTotal_HP());
        System.out.printf("Moedas: %d%n", personagem.getCoins());
        System.out.printf("Nivel: %d%n", personagem.getLevel());
        System.out.println("Seu pai foi morto na sua frente por um trupe de bandidos misteriosos, demorou anos mas vc finalmento os rastreou até uma masmorra. Ao entrar na masmorra a primeira coisa q vc vê é um guarda monstruoso que te ataca imadiatamente sem tempo de reação");
        personagem.Receber_Dano();
        System.out.printf("vc tomou 1d20 de dano, agora vc esta com %d de vida%n", personagem.getCurrent_HP());
        System.out.println("por pouco vc corre para mais fundo da masmorra com vida, no caminnho vc encontra ervas medicinais curativas, vc as reconhece de uma vez q seu levou-o para caçar, sem exitar, vc as passa em seus ferimentos.");
        personagem.Recuperar_Vida();
        System.out.printf("vc recuperou 1d20 de vida e agora esta com %d de vida%n", personagem.getCurrent_HP());
        System.out.println("Logo ao lado das ervas vc encontra algo brilhante e reluzente... 23 moedas de ouro");
        personagem.Receber_Moedas(23);
        System.out.printf("Agora vc tem %d moedas%n", personagem.getCoins());
        System.out.println("Vc volta a andar pela masmorra escura, com medo que o guarda te encontre, mas não demora muito até achar outra coisa que o intriga, um homem... alto, magro, vestindo um terno roxo com calças brancas e em sua cabeça, uma mascara de gato roxa, cobrindo a sua cabeça por completo. Ele pergunta se gostaria de comprar alguma coisa antes mesmo de se apresentar... Vc decide aceitar, e ele mostra a sua pequena loja escondida em seu terno");

        boolean lojaAberta = true;

        while (lojaAberta) {

            System.out.println("\n===== LOJA =====");
            System.out.printf("Você possui %d moedas.%n", personagem.getCoins());

            System.out.println("1 - Poção de vida - 40 moedas");
            System.out.println("2 - Espada grande - 140 moedas");
            System.out.println("3 - Um beijo - 10 moedas");
            System.out.println("4 - Poção de dano - 90 moedas");
            System.out.println("5 - Sair de perto dele");
            System.out.print("Escolha uma opção: ");
            int escolha = scanner.nextInt();

            switch (escolha) {

                case 1:
                    if (personagem.getCoins() >= 40) {
                        personagem.Gastar_Moedas(40);
                        System.out.println("Você comprou uma poção de vida, vc decice toma-la instantaneamente");
                        personagem.Recuperar_Vida();
                        System.out.printf("agora vc tem %d pontos de vida", personagem.getCurrent_HP());
                    } else {
                        System.out.println("Você não possui moedas suficientes.");
                    }
                    break;

                case 2:
                    if (personagem.getCoins() >= 140) {
                        personagem.Gastar_Moedas(140);
                        System.out.println("Você comprou uma espada grande.");
                    } else {
                        System.out.println("Você não possui moedas suficientes.");
                    }
                    break;

                case 3:
                    if (personagem.getCoins() >= 10) {
                        personagem.Gastar_Moedas(10);
                        System.out.println("Você comprou um beijo, o gato aproxima-se de vc com seu cheiro amadeirado e lhe beija sem demosntrar emoções, e volta ate olhar seriamente");
                    } else {
                        System.out.println("Você não possui moedas suficientes.");
                    }
                    break;

                case 4:
                    if (personagem.getCoins() >= 90) {
                        personagem.Gastar_Moedas(90);
                        System.out.println("Você comprou uma poção de dano, pensando ser uma poção de vida, vc decide toma-la instantaneamente");
                        personagem.Receber_Dano();
                        personagem.Receber_Dano();
                        personagem.Receber_Dano();
                        personagem.Receber_Dano();
                        personagem.Receber_Dano();
                        System.out.printf("O gato olha pra vc com desaprovação, 'talvez vc seja mais burro doq eu imaginei... diz o gato', agora vc esta com %d pontos de vida", personagem.getCurrent_HP());
                    } else {
                        System.out.println("Você não possui moedas suficientes.");
                    }
                    break;

                case 5:
                    lojaAberta = false;
                    System.out.println("Você sai de perto do gato, até que seu cheiro amadeirado suma completamente...");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }
        }

        System.out.println("Depois de toda essa aventura, vc imagina poder subir de nivel, mas o mestre NEGA. Depois de 15 mins discutindo e barganhando, o mestre finalmente concede mais um nivel pro seu persongem.");

        personagem.Subir_Nivel();

        System.out.println("ESTADO DO SEU PERSONAGEM NO FINAL DA SESSÃO:");
        System.out.printf("Nome: %s%n", personagem.getName());
        System.out.printf("Classe: %s%n", personagem.getClasse());
        System.out.printf("Vida: %d/%d%n", personagem.getCurrent_HP(), personagem.getTotal_HP());
        System.out.printf("Moedas: %d%n", personagem.getCoins());
        System.out.printf("Nivel: %d%n", personagem.getLevel());

        scanner.close();*/
    }
}