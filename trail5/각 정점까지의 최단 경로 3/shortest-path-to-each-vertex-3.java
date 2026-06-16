import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();

        ArrayList<int[]>[] edges = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), d = sc.nextInt();
            edges[u].add(new int[]{v, d});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((e1, e2) -> e1[0] - e2[0]);
        pq.add(new int[]{0, 1});

        int[] dists = new int[n + 1];
        Arrays.fill(dists, Integer.MAX_VALUE);
        dists[1] = 0;

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            if (curr[0] != dists[curr[1]]) continue;
            for (int[] edge : edges[curr[1]]) {
                int newDist = curr[0] + edge[1];
                if (newDist < dists[edge[0]]) {
                    dists[edge[0]] = newDist;
                    pq.add(new int[]{newDist, edge[0]});
                }
            }
        }

        for (int i = 2; i <= n; i++) {
            System.out.println(dists[i] != Integer.MAX_VALUE ? dists[i] : -1);
        }
    }
}