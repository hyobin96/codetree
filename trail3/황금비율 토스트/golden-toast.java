import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        LinkedList<Character> list = new LinkedList<>();
        int n = sc.nextInt(), m = sc.nextInt();
        String input = sc.next();
        for (char c : input.toCharArray()) {
            list.addLast(c);
        }

        ListIterator<Character> it = list.listIterator(list.size());
        for (int i = 0; i < m; i++) {
            String command = sc.next();

            switch (command) {
                case "L":
                    if (it.hasPrevious()) it.previous();
                    break;
                case "R":
                    if (it.hasNext()) it.next();
                    break;
                case "D":
                    if (it.hasNext()) {
                        it.next();
                        it.remove();
                    }
                    break;
                case "P":
                    it.add(sc.next().charAt(0));
                    break;
            }            
        }

        list.stream().forEach(System.out::print);

    }
}