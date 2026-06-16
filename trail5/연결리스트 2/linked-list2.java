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

        HashMap<Integer, Node> map = new HashMap<>();
        for (int i = 1; i <= n; i++){
            map.put(i, new Node(i));
        }

        int q = sc.nextInt();

        for (int i = 0; i < q; i++) {
            int command = sc.nextInt();
            Node node;

            switch (command) {
                case 1:
                    node = map.get(sc.nextInt());
                    if (node.prev != null) {
                        node.prev.next = node.next;
                    }
                    if (node.next != null) {
                        node.next.prev = node.prev;
                    }
                    node.prev = node.next = null;
                    break;
                case 2:
                    node = map.get(sc.nextInt());
                    insertPrev(node, map.get(sc.nextInt()));
                    break;
                case 3:
                    node = map.get(sc.nextInt());
                    insertNext(node, map.get(sc.nextInt()));
                    break;
                case 4:
                    node = map.get(sc.nextInt());
                    int prev = node.prev != null ? node.prev.data : 0;
                    int next = node.next != null ? node.next.data : 0;
                    System.out.println(prev + " " + next);
                    break;
            }
        }

        for (int i = 1; i <= n; i++) {
            Node node = map.get(i);
            System.out.print((node.next != null ? node.next.data : 0) + " ");
        }
        

    }

    // null node1 null
    // node node1 node
    // node node2 node1 node
    static void insertPrev(Node node1, Node node2) {
        node2.prev = node1.prev;
        node2.next = node1;
        node1.prev = node2;
        if (node2.prev != null) {
            node2.prev.next = node2;
        }
    }

    // null node1 null
    // node node1 node
    // node node1 node2 node
    static void insertNext(Node node1, Node node2) {
        node2.next = node1.next;
        node2.prev = node1;
        node1.next = node2;
        if (node2.next != null) {
            node2.next.prev = node2;
        }
    }
}