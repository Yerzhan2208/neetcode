---
id: "110"
title: Balanced Binary Tree
difficulty: 🟢 Easy
pattern: Binary Tree
leetcode_url: https://leetcode.com/problems/balanced-binary-tree/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-22
---

## 🎯 Core Intuition
My solution was similar to finding the diameter, but this time just checked if the difference between heights are less or equal than 1 and checked if it's true for left child and right child.

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 \
                and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.height(root.left) + 1
        right = self.height(root.right) + 1
        return max(left, right)
```