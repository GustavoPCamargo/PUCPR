import java.util.Random;
import java.util.Scanner;
import java.util.ArrayList;

public class aprendendo {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        ArrayList<String> lista = new ArrayList<>();

        System.out.print("Diga o tamanho da lista: ");
        int tamanho = scanner.nextInt();

        listaAleatoria(lista, tamanho, random);

        System.out.println(lista);

        scanner.close();
    }

    public static void listaAleatoria(ArrayList<String> lista, int tamanho, Random random) {

        for (int i = 0; i < tamanho; i++) {

            int num = random.nextInt(100) + 1;

            if (num % 2 == 0) {
                lista.add(num + " - número é par");
            } else if (num % 3 == 0) {
                lista.add(num + " - número é múltiplo de 3");
            } else {
                lista.add(num + " - é ímpar");
            }
        }
    }
}