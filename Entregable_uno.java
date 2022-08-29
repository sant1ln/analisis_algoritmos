
// Java program to sort an array
// using bucket sort
import java.util.*;
import java.util.Collections;

class Entregable_uno {

    // Function to sort arr[] of size n
    // using bucket sort
    static void bucketSort(float arr[], int n) {
        if (n <= 0)
            return;

        // 1) Create n empty buckets
        @SuppressWarnings("unchecked")
        Vector<Float>[] buckets = new Vector[n];

        for (int i = 0; i < n; i++) {
            buckets[i] = new Vector<Float>();
        }

        // 2) Put array elements in different buckets
        for (int i = 0; i < n; i++) {
            float idx = arr[i] * n;
            buckets[(int) idx].add(arr[i]);
        }

        // 3) Sort individual buckets
        for (int i = 0; i < n; i++) {
            Collections.sort(buckets[i]);
        }

        // 4) Concatenate all buckets into arr[]
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < buckets[i].size(); j++) {
                arr[index++] = buckets[i].get(j);
            }
        }
    }

    static float[] randomNumbers(int limit) {
        float[] arr = new float[limit];
        for (int k = 0; k < limit; k++) {
            Random rd = new Random();
            arr[k] = rd.nextFloat();
        }
        return arr;
    }

    // Driver code
    public static void main(String args[]) {
        
        int datos[] = { 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 };
        double[] tiempos = new double[datos.length];

        for (int i = 0; i < datos.length; i++) {

            float arr[] = randomNumbers(datos[i]);
            int n = arr.length;
            long inicio = System.nanoTime();
            bucketSort(arr, n);
            long fin = System.nanoTime();
            double tiempo = (double) ((fin - inicio)/1);
            tiempos[i] = tiempo;

            /* System.out.println("Sorted array is ");
            for (float el : arr) {
                System.out.print(el + " ");
            } */

        }

        System.out.print(Arrays.toString(tiempos));
        
    }
}
