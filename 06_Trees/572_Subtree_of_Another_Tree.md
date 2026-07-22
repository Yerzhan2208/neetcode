---
id: "572"
title: Subtree of Another Tree
difficulty: 🟢 Easy
pattern: Binary Tree
leetcode_url: https://leetcode.com/problems/subtree-of-another-tree/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-22
---

## 🎯 Core Intuition
If we use the isSameTree function from the previous problem, this one becomes easier. We just compare root and subRoot, then progress to the root's children and compare them with subRoot.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) \
		        and self.isSameTree(p.right, q.right)
```