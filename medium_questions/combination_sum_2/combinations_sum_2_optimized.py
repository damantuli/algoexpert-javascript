
class Solution:

    def findCominations2(self, index: int ,candidates: list [int], target: int, ans: list [list[int]], ds: list[int]):
        if target == 0:
            ans.append(list(ds))
            return
        
        for i in range(index, len(candidates)):
            if i> index and candidates[i] == candidates[i-1]:
                continue
            if candidates[i]> target:
                break

            ds.append(candidates[i])
            self.findCominations2(i+1, candidates, target-candidates[i], ans, ds)
            ds.pop()

    def combinationSum2(self, candidates: list[int], target):
        ans = []
        candidates.sort()
        self.findCominations2(0, candidates, target, ans, [])
        return ans
    