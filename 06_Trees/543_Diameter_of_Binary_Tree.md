---
id: "543"
title: Diameter of Binary Tree
difficulty: 🟢 Easy
pattern: DFS
leetcode_url: https://leetcode.com/problems/diameter-of-binary-tree/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-22
---

## 🎯 Core Intuition
My solution was to calculate the height of the right node and the left node and then sum them up. Also compare it with the sum for the left child and right child, thus we get the max diameter. Other approach could be DFS.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.height(root.right) + self.height(root.left), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right));

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.height(root.left) + 1
        r = self.height(root.right) + 1
        return max(l, r)
```