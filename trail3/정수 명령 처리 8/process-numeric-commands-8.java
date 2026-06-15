import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Integer n = sc.nextInt();
        
        LinkedList<Integer> list = new LinkedList<>();

        for (int i = 0; i < n; i ++) {
            String command = sc.next();
            Integer result = null;
            switch (command) {
                case "push_front":
                    list.addFirst(sc.nextInt());
                    break;
                case "push_back":
                    list.addLast(sc.nextInt());
                    break;
                case "pop_front":
                    result = list.pollFirst();
                    break;
                case "pop_back":
                    result = list.pollLast();
                    break;
                case "size":
                    result = list.size();
                    break;
                case "empty":
                    result = list.isEmpty() ? 1 : 0;
                    break;
                case "front":
                    result = list.peekFirst();
                    break;
                case "back":
                    result = list.peekLast();
                    break;
            }
            if (result != null) {
                System.out.println(result);
            }
        }
    }
}