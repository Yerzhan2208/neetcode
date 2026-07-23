---
id: "102"
title: Binary Tree Level Order Traversal
difficulty: 🟡 Medium
pattern: Stack
leetcode_url: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of tree
space_complexity: O(n) - length of tree
date_created: 2026-07-23
---

## 🎯 Core Intuition
My thought was BFS straight, just by finding all the values for the level, we can construct list to add to result. So, I used stack with root, then added all the values of his children to the stack and changed the stack to new one with children nodes, then appended the array to the resulting list. This way, I got the resulting array with each level.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        res = [[root.val]]
        while stack:
            arr = []
            new_stack = []
            for i in stack:
                if i.left and i.right:
                    arr.append(i.left.val)
                    arr.append(i.right.val)
                    new_stack.append(i.left)
                    new_stack.append(i.right)
                elif i.left:
                    arr.append(i.left.val)
                    new_stack.append(i.left)
                    continue
                elif i.right:
                    arr.append(i.right.val)
                    new_stack.append(i.right)
                    continue
                
            stack = new_stack
            if arr == []:
                break
            res.append(arr)
        return res
```
## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        current_level = [root]

        while current_level:
            # Record current level values
            res.append([node.val for node in current_level])

            # Build the next level
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level

        return res
```
