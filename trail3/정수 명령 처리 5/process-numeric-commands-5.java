import java.util.*;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.
        sc.nextLine();

        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] input = sc.nextLine().split(" ");

            switch (input[0]){
                case "push_back":
                    list.add(Integer.valueOf(input[1]));
                    break;
                case "get":
                    int k = Integer.valueOf(input[1]);
                    if (list.size() >= k)
                    System.out.println(list.get(k - 1));
                    break;
                case "size":
                    System.out.println(list.size());
                    break;
                case "pop_back":
                    list.remove(list.size() - 1);
                    break;
            }

        }
    }
}