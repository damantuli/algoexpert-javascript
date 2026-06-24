from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def findCombination(index: int, target: int, ds: List[int]):
            if index == len(candidates):
                if target == 0:
                    ans.append(list(ds))
                return
            
            if candidates[index] <= target:
                ds.append(candidates[index])
                findCombination(index, target - candidates[index], ds)
                ds.pop()
            
            findCombination(index + 1, target, ds)
            
        findCombination(0, target, [])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print("Test case 1 (candidates=[2, 3, 6, 7], target=7):", sol.combinationSum([2, 3, 6, 7], 7))
    print("Test case 2 (candidates=[2, 3, 5], target=8):", sol.combinationSum([2, 3, 5], 8))
    print("Test case 3 (candidates=[2], target=1):", sol.combinationSum([2], 1))
                