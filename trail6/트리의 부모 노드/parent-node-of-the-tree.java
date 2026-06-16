import java.util.*;

public class Main {

    static boolean[] visited;
    static ArrayList<Integer>[] edges;

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        edges = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }

        for (int i = 2; i <= n; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            edges[u].add(v);
            edges[v].add(u);
        }

        visited = new boolean[n + 1];
        int[] parents = new int[n + 1];
        dfs(1, parents);

        for (int i = 2; i <= n; i++) {
            System.out.println(parents[i]);
        }
        
    }

    static void dfs(int u, int[] parents) {
        for (int v : edges[u]) {
            if (visited[v]) continue;
            parents[v] = u;
            visited[u] = true;
            dfs(v, parents);
        }
    }
}