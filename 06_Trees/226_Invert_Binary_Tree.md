---
id: "226"
title: Invert Binary Tree
difficulty: 🟢 Easy
pattern: Binary Tree
leetcode_url: https://leetcode.com/problems/invert-binary-tree/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-22
---

## 🎯 Core Intuition
The base case is when the root is None, then we return None. Then the main action is to switch nodes: right, left = left, right and do the same for the child nodes. The resulting tree will be inverted and we return its root.

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root