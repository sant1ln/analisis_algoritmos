/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



package entregable_dos;
import java.util.*;
import java.util.Collections;
import java.util.concurrent.ThreadLocalRandom;
import java.util.LinkedList;
/**
 *
 * @author ESTUDIANTE
 */
public class Entregable_dos {

    node head;
    node sorted;

    class node {

        int val;
        node next;

        public node(int val) {
            this.val = val;
        }
    }

    void push(int val) {
        /* allocate node */
        node newnode = new node(val);
        /* link the old list off the new node */
        newnode.next = head;
        /* move the head to point to the new node */
        head = newnode;
    }
    
    
    void deleteList()
    {
        head = null;
    }

    // function to sort a singly linked list using insertion sort
    void insertionSort(node headref) {
        // Initialize sorted linked list
        sorted = null;
        node current = headref;
        // Traverse the given linked list and insert every
        // node to sorted
        while (current != null) {
            // Store next for next iteration
            node next = current.next;
            // insert current in sorted linked list
            sortedInsert(current);
            // Update current
            current = next;
        }
        // Update head_ref to point to sorted linked list
        head = sorted;
    }

    /*
	* function to insert a new_node in a list. Note that
	* this function expects a pointer to head_ref as this
	* can modify the head of the input linked list
	* (similar to push())
     */
    void sortedInsert(node newnode) {
        /* Special case for the head end */
        if (sorted == null || sorted.val >= newnode.val) {
            newnode.next = sorted;
            sorted = newnode;
        } else {
            node current = sorted;
            /* Locate the node before the point of insertion */
            while (current.next != null && current.next.val < newnode.val) {
                current = current.next;
            }
            newnode.next = current.next;
            current.next = newnode;
        }
    }

    /* Function to print linked list */
    void printlist(node head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
    }
    
    static int randomNumber() {
        int randNumber = ThreadLocalRandom.current().nextInt(1, 1000 + 1);
        return randNumber;
    }

    // Driver program to test above functions
    public static void main(String[] args) {
        
        Entregable_dos list = new Entregable_dos();
        int datos[] = { 10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};
        double[] tiempos = new double[datos.length];
        
        for (int i = 0; i < datos.length;i++){   
            for (int j = 0; j < datos[i]; j++) {
                int randNumber = randomNumber();
                list.push(randNumber);
            }
            long inicio = System.nanoTime();
            list.insertionSort(list.head);            
            long fin = System.nanoTime();
            double tiempo = (double) ((fin - inicio));
            tiempos[i] = tiempo;         
            list.deleteList();          
        }
        
        System.out.println(Arrays.toString(tiempos));
    }
}
