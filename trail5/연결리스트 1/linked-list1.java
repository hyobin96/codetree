import java.util.*;
import java.io.*;

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
    public static void main(String[] args) throws IOException{
        // Please write your code here.
        Scanner sc = new Scanner(System.in);    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // String init = sc.next();
        String init = br.readLine();
        int n = Integer.valueOf(br.readLine());
        Node curr = new Node(init);

        for (int i = 0; i < n; i++) {
            String[] command = br.readLine().split(" ");

            switch (Integer.valueOf(command[0])) {
                case 1:
                    curr.insertPrev(new Node(command[1]));
                    break;
                case 2:
                    curr.insertNext(new Node(command[1]));
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