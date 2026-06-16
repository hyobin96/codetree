import java.util.*;

class Node {
    String data;
    Node prev, next;
    public Node(String data) {
        this.data = data;
        prev = next = null;
    }
}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), q = sc.nextInt();
        
        Node node = new Node(sc.next());
        Node cur = node;
        for(int i = 1; i < n; i++) {
            Node newNode = new Node(sc.next());
            node.next = newNode;
            newNode.prev = node;
            node = node.next;
        }
        node.next = cur;
        cur.prev = node;

        // while (cur != null) {
        //     System.out.println(cur.data);
        //     cur = cur.next;
        // }

        for (int i = 0; i < q; i++) {
            int command = sc.nextInt();
            switch (command) {
                case 1:
                    if (cur.next != null) cur = cur.next;
                    break;
                case 2:
                    if (cur.prev != null) cur = cur.prev;
                    break;
                case 3:
                    if (cur.next != null) {
                        cur.next = cur.next.next;
                        cur.next.prev = cur;
                    }
                    break;
                case 4:
                    Node newNode = new Node(sc.next());
                    if (cur.next != null) {
                        cur.next.prev = newNode;
                        newNode.next = cur.next;
                    }
                    newNode.prev = cur;
                    cur.next = newNode;
                    break;
            }
            if (cur.prev == cur.next) System.out.println(-1);
            else if (cur.prev == null) System.out.println(-1);
            else {
                System.out.println(cur.prev.data + " " + cur.next.data);
            }
        }
    }
}