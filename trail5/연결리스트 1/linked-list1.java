import java.util.*;
import java.io.*;

class Node<E> {
    E data;
    Node<E> prev, next;

    public Node(E data) {
        this.data = data;
        prev = next = null;
    }
}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String init = sc.next();

        Node<String> head = new Node<>("(Null)");
        Node<String> tail = new Node<>("(Null)");

        Node<String> cur = new Node<>(init);
        head.next = cur;
        cur.prev = head;
        cur.next = tail;
        tail.prev = cur;

        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int command = sc.nextInt();
            StringBuilder builder = new StringBuilder();
            Node<String> newNode;
            switch (command) {
                case 1:
                    newNode = new Node<>(sc.next());
                    newNode.prev = cur.prev;
                    newNode.next = cur;
                    cur.prev.next = newNode;
                    cur.prev = newNode;
                    break;
                case 2:
                    newNode = new Node<>(sc.next());
                    newNode.next = cur.next;
                    newNode.prev = cur;
                    cur.next.prev = newNode;
                    cur.next = newNode;
                    break;
                case 3:
                    if (cur.prev != head) cur = cur.prev;
                    break;
                case 4:
                    if (cur.next != tail) cur = cur.next;
                    break;
            }
            builder.append(cur.prev.data + " " + cur.data + " " + cur.next.data);
            System.out.println(builder.toString());
        }
    }
}