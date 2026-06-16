import java.util.*;

class Node {
    int data;
    Node prev, next;
    public Node(int data) {
        this.data = data;
    }
}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int q = sc.nextInt();

        Node[] nodes = new Node[n + 1];
        for (int i = 1; i <= n; i++) {
            nodes[i] = new Node(i);
        }

        for (int i = 1; i < n; i++) {
            link(nodes[i], nodes[i + 1]);
        }

        // Node head = nodes[1];
        // while (head != null) {
        //     System.out.print(head.data + " ");
        //     head = head.next;
        // }

        // n a b n c d n
        // n c d n
        // n a b c d n
        for (int i = 0; i < q; i++) {
            int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(), d = sc.nextInt();
            Node aPrevNode = nodes[a].prev;
            Node bNextNode = nodes[b].next;
            Node cPrevNode = nodes[c].prev;
            Node dNextNode = nodes[d].next;
            if (nodes[b].next == nodes[c]) {
                unlink(nodes[b], nodes[c]);
                link(nodes[d], nodes[a]);
                link(nodes[b], dNextNode);
                link(aPrevNode, nodes[c]);
                continue;
            }
            // n c d a b n
            if (nodes[d].next == nodes[a]) {
                unlink(nodes[d], nodes[a]);
                link(nodes[b], nodes[c]);
                link(nodes[d], bNextNode);
                link(cPrevNode, nodes[a]);
                continue;
            }
            
            link(cPrevNode, nodes[a]);
            link(nodes[b], dNextNode);
            link(aPrevNode, nodes[c]);
            link(nodes[d], bNextNode);
        }

        Node head = nodes[1];
        while (head.prev != null) {
            head = head.prev;
        }

        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
    }

    static void link(Node n1, Node n2) {
        if (n1 != null) n1.next = n2;
        if (n2 != null) n2.prev = n1;
    }

    static void unlink(Node n1, Node n2) {
        if (n1 != null) n1.next = null;
        if (n2 != null) n2.prev = null;
    }
}