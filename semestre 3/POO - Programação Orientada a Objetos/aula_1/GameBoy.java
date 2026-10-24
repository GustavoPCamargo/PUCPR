package aula_1;

import java.util.Scanner;

public class GameBoy {

    public String cor;
    public float tamanho;
    public boolean taligado;
    public int bateria;
    public int modelo;

    public void ligar(){
        System.out.printf("vc ligou o GameBoy e vc tem %d%% de bateria ", bateria);
    }

    public void desligar(){
        System.out.println("Vc desligou o gameboy");
    }

    public void novo_jogo(){
        System.out.println("Vc criou um novo jogo");
    }

    public static void main(String[] args) {
        GameBoy gameboy = new GameBoy();
        Scanner scanner = new Scanner(System.in);

        System.out.print("vc que ligar o gameboy? ");
        String decisão = scanner.nextLine();
        scanner.close();

        gameboy.bateria = 100;

        if (decisão == "sim"){
            System.out.println("ok");
            gameboy.ligar();
        }
        //gameboy.novo_jogo();
        //gameboy.desligar();
    }

}