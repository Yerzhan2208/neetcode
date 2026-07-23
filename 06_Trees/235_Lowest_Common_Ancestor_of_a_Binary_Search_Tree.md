---
id: "235"
title: Lowest Common Ancestor of a Binary Search Tree
difficulty: 🟡 Medium
pattern: BST
leetcode_url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
status: 🟨 Reviewing
time_complexity: O(h) - h is height of the tree
space_complexity: O(h) - h is height of the tree
date_created: 2026-07-23
---

## 🎯 Core Intuition
If it is the BST, the numbers on the left of the root are smaller than the root, the numbers on the right are larger. So, we can recursively compare if the max value of p and q is smaller than root, we move root to the left child, if the min value of p and q is larger than root, we move root to the right.
Another approach could be iterative

## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None

        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```