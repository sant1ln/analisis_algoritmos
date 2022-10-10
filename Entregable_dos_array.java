/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package com.mycompany.entregable_dos;

import java.util.concurrent.ThreadLocalRandom;
import java.util.*;
import java.util.Collections;

/**
 *
 * @author Santiago
 */
class Entregable_dos {

    /*Function to sort array using insertion sort*/

    static int[] randomNumbers(int limit) {
        int[] arr = new int[limit];
        for (int k = 0; k < limit; k++) {
            arr[k] = ThreadLocalRandom.current().nextInt(1, 50 + 1);
        }
        return arr;
    }

    // Driver method
    public static void main(String args[]) {
        int datos[] = {10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};
        double[] tiempos = new double[datos.length];
        /*Function to sort array using insertion sort*/
        for (int i = 0; i < datos.length; i++) {

            int arr[] = randomNumbers(datos[i]);
            long inicio = System.nanoTime();
            //Insertion sort 
            int n = arr.length;
            for (int k = 1; k < n; ++k) {
                int key = arr[k];
                int j = k - 1;

                /* Move elements of arr[0..i-1], that are
               greater than key, to one position ahead
               of their current position */
                while (j >= 0 && arr[j] > key) {
                    arr[j + 1] = arr[j];
                    j = j - 1;
                }
                arr[j + 1] = key;
            }
            long fin = System.nanoTime();
            double tiempo = (double) ((fin - inicio) / 1);
            tiempos[i] = tiempo;
        }
        System.out.print(Arrays.toString(tiempos));

    }
}
