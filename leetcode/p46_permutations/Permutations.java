package p46_permutations;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Permutations {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int[] nums = Arrays.stream(line.split(","))
                           .map(String::trim)
                           .mapToInt(Integer::parseInt)
                           .toArray();
        /*
        List<Integer> nums = Arrays.stream(line.split(","))
                                   .map(String::trim)
                                   .map(Integer::parseInt)
                                   .collect(Collectors.toList());
        */
        System.out.println(permute(nums));
    }

    public static List<List<Integer>> permute(int[] nums) {
        Set<Integer> used = new HashSet<>();
        List<Integer> curr = new ArrayList<>();
        List<List<Integer>> answer = new ArrayList<>();
        backtrack(curr, nums, used, answer);
        return answer;
    }

    public static void backtrack(List<Integer> curr, int[] nums, Set<Integer> used,
                                 List<List<Integer>> answer) {
        if (curr.size() == nums.length) {
            answer.add(new ArrayList<>(curr));
            return;
        }

        for (int num : nums) {
            if (used.contains(num)) {
                continue;
            }
            curr.add(num);
            used.add(num);
            backtrack(curr, nums, used, answer);
            used.remove(num);
            curr.remove(curr.size() - 1);
        }
    }
}
