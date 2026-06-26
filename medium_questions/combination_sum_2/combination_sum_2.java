package combination_sum_2;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class Solution {
    public void findCombination2(int index, int[] candidates, int target, HashSet<List<Integer>> ans,
            List<Integer> ds) {
        if (index == candidates.length) {
            if (target == 0) {
                ans.add(new ArrayList<>(ds));
            }
            return;
        }

        if (candidates[index] <= target) {
            ds.add(candidates[index]);
            findCombination2(index + 1, candidates, target - candidates[index], ans, ds);
            ds.remove(ds.size() - 1);
        }
        findCombination2(index + 1, candidates, target, ans, ds);
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        HashSet<List<Integer>> ans = new HashSet<>();
        Arrays.sort(candidates);
        findCombination2(0, candidates, target, ans, new ArrayList<>());
        List<List<Integer>> result = new ArrayList<>(ans);
        return result;
    }

}
