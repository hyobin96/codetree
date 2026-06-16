import java.util.*;

class Node {
    String data;
    Node prev, next;
    public Node(String data) {
        this.data = data;
        this.prev = this.next = null;
    }

    // prev  new  cur
    public void insertPrev(Node newNode) {
        newNode.next = this;
        newNode.prev = this.prev;
        this.prev = newNode;

        if (newNode.prev != null) {
            newNode.prev.next = newNode;
        }
    }

    // cur new next
    public void insertNext(Node newNode) {
        newNode.prev = this;
        newNode.next = this.next;
        this.next = newNode;

        if (newNode.next != null) {
            newNode.next.prev = newNode;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);    

        String init = sc.next();
        int n = sc.nextInt();
        Node curr = new Node(init);

        for (int i = 0; i < n; i++) {
            int command = sc.nextInt();

            switch (command) {
                case 1:
                    curr.insertPrev(new Node(sc.next()));
                    break;
                case 2:
                    curr.insertNext(new Node(sc.next()));
                    break;
                case 3:
                    if (curr.prev != null) {
                        curr = curr.prev;
                    }
                    break;
                case 4:
                    if (curr.next != null) {
                        curr = curr.next;
                    }
                    break;
            }
            StringBuilder builder = new StringBuilder();
            builder.append((curr.prev != null ? curr.prev.data : "(Null)") + " ");
            builder.append(curr.data + " ");
            builder.append(curr.next != null ? curr.next.data : "(Null)");
            System.out.println(builder);
        }
    }
}