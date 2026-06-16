import java.util.*;

class DoublyLinkedList {
    static class Node {
        int data;
        Node prev, next;
        public Node(int data) {
            this.data = data;
            prev = next = null;
        }
    }

    int size = 0;
    Node head, tail;
    public DoublyLinkedList() {
        head = new Node(0);
        tail = new Node(0);
        head.next = tail;
        tail.prev = head;
    }

    // head node
    public int removeFirst() {
        if (size == 0) return 0;
        Node FirstNode = head.next;
        head.next = FirstNode.next;
        head.next.prev = head;
        FirstNode.prev = FirstNode.next = null;
        size--;
        return FirstNode.data;
    }

    // node tail
    public int removeLast() {
        if (size == 0) return 0;
        Node lastNode = tail.prev;
        tail.prev = lastNode.prev;
        tail.prev.next = tail;
        lastNode.prev = lastNode.next = null;
        size--;
        return lastNode.data;
    }

    // head newNode node
    public void addFirst(int data) {
        if (data == 0) return;
        Node newNode = new Node(data);
        newNode.next = head.next;
        head.next = newNode;
        newNode.prev = head;
        newNode.next.prev = newNode;
        size++;
    }

    // node newNode tail
    public void addLast(int data) {
        if (data == 0) return;
        Node newNode = new Node(data);
        newNode.next = tail;
        newNode.prev = tail.prev;
        newNode.prev.next = newNode;
        tail.prev = newNode;
        size++;
    }

    public void addLastList(DoublyLinkedList dl) {
        tail.prev.next = dl.head.next;
        dl.head.next.prev = tail.prev;
        tail = dl.tail;
        size += dl.size;
    }

    public void addFirstList(DoublyLinkedList dl) {
        dl.tail.prev.next = head.next;
        head.next.prev = dl.tail.prev;
        head = dl.head;
        size += dl.size;
    }

    public String toString() {
        StringBuilder builder = new StringBuilder();
        Node cur = head.next;
        while (cur != tail) {
            builder.append(cur.data + " ");
            cur = cur.next;
        }
        return builder.toString();
    }

}

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();

        DoublyLinkedList[] lists = new DoublyLinkedList[k + 1];
        for (int i = 1; i <= k; i++) {
            lists[i] = new DoublyLinkedList();
        }

        for (int i = 1; i <= n; i++) {
            lists[1].addLast(i);
        }

        int q = sc.nextInt();
        for (int l = 0; l < q; l++) {
            int command = sc.nextInt(), i = sc.nextInt(), j = sc.nextInt();
            switch (command) {
                case 1:
                    lists[j].addLast(lists[i].removeFirst());
                    break;
                case 2:
                    lists[j].addFirst(lists[i].removeLast());
                    break;
                case 3:
                    if (i == j) break;
                    lists[j].addFirstList(lists[i]);
                    lists[i] = new DoublyLinkedList();
                    break;
                case 4:
                    if (i == j) break;
                    lists[j].addLastList(lists[i]);
                    lists[i] = new DoublyLinkedList();
                    break;
            }
            // for (int m = 1; m <= k; m++) {
            //     System.out.println(lists[m].size + " " + lists[m]);
            // }
        }

        for (int i = 1; i <= k; i++) {
            System.out.println(lists[i].size + " " + lists[i]);
        }
    }
}