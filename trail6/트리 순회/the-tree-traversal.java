import java.util.*;

class Node {
    int c1 = -1, c2 = -1;
}

public class Main {
    static Node[] tree;

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        tree = new Node[n * 2 + 2];
        for (int i = 0; i < tree.length; i++) {
            tree[i] = new Node();
        }
        
        for (int i = 0; i < n; i++) {
            int p = sc.next().charAt(0) - 'A';
            
            int c1 = sc.next().charAt(0) - 'A';
            int c2 = sc.next().charAt(0) - 'A';
            if (c1 >= 0) tree[p].c1 = c1;
            if (c2 >= 0) tree[p].c2 = c2;
        }

        preOrder(0);
        System.out.println();

        inOrder(0);
        System.out.println();

        postOrder(0);
    }

    static void preOrder(int u) {
        if (u == -1) return;
        System.out.print((char)(u + 'A'));
        preOrder(tree[u].c1);
        preOrder(tree[u].c2);
    }

    static void inOrder(int u) {
        if (u == -1) return;
        inOrder(tree[u].c1);
        System.out.print((char)(u + 'A'));
        inOrder(tree[u].c2);
    }

    static void postOrder(int u){
        if (u == -1) return;
        postOrder(tree[u].c1);
        postOrder(tree[u].c2);
        System.out.print((char)(u + 'A'));
    }
}