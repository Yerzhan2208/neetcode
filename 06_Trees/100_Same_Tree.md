---
id: "100"
title: Same Tree
difficulty: 🟢 Easy
pattern: Binary Tree
leetcode_url: https://leetcode.com/problems/same-tree/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-22
---

## 🎯 Core Intuition
At first, we should check the base cases, if both of them are None, then return True. Then, if one of them is None, the other is not - return False. At the end, we just compare the value in p and q trees and progress by calling function to check left children and right children.

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) \
		        and self.isSameTree(p.right, q.right)