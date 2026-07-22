---
id: "104"
title: Maximum Depth of Binary Tree
difficulty: 🟢 Easy
pattern: DFS
leetcode_url: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-22
---

## 🎯 Core Intuition
We can save the result in res variable and pass it to the dfs for comparing. In dfs function, the base case is if root is None, then we return 0. Then, the step will be to go left and then right calculating the depth by incrementing these both. The result is the maximum of the left and right. We call the dfs and then return the maximum depth.

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            res = max(left, right)
            return res

        return dfs(root)