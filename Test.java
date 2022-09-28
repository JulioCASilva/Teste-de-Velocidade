public class Test{
  public static void main(String[] args) {
    System.out.println("Olá mundo"); /*imprimir ola mundo */

      /*inicio do contador de 1 ate 1000 */
      System.out.println("Iniciando contagem:");
    for (int count=1 ; count <=1000 ; count++){
      System.out.print(" " + count);
        }
      /*final do contador de 1 ate 1000 */

      /*inicio do contador de tempo de duração */
long inicio = System.nanoTime();
  int x = 0;

while (x < 100000000) {
     x = x + 1;
    }

long fim = System.nanoTime();
long total = (fim - inicio)/1000000000;
 System.out.println(" " + "Tempo total: " + ((double)(fim-inicio)/1000000000.0));
    }
    /*final do contador de tempo de duração */
}
