def subsets(nums: list) -> list[list]:
    """
    Generate all possible subsets of the given list using backtracking.
    Time Complexity: O(2^n), Space Complexity: O(n)
    """
    res = []

    def dfs(index: int, path: list):
        # Base case: reached end of array, save current subset
        if index == len(nums):
            res.append(path.copy())  # Copy to avoid reference issues
            return
        
        # Decision 1: Include current element in subset
        path.append(nums[index])
        dfs(index+1, path)  # Recurse with element included

        # Backtrack: Remove element to explore other possibilities
        path.pop()

        # Decision 2: Exclude current element from subset
        dfs(index+1, path)  # Recurse without element
    
    # Start DFS from index 0 with empty path
    dfs(0, [])
    return res


for res in subsets([1,2,3]): print(res)