---
id: "199"
title: Binary Tree Right Side View
difficulty: 🟡 Medium
pattern: Stack
leetcode_url: https://leetcode.com/problems/binary-tree-right-side-view/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-23
---

## 🎯 Core Intuition
The solution is the same as for the Level Order Traversal, just at the end we need to return the last element of each level of the tree. The same can be applied for the left side view, we need to return just the first element.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        currentLevel = [root]

        while currentLevel:
            res.append([node.val for node in currentLevel])

            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return [x[-1] for x in res]
```