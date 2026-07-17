---
id: "150"
title: Evaluate Reverse Polish Notation
difficulty: 🟡 Medium
pattern: Stack
leetcode_url: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
status: 🟩 Mastered
time_complexity: O(n) - length of array
space_complexity: O(n) - length of stack
date_created: 2026-07-17
---

## 🎯 Core Intuition
This is a sample problem related to stack, if there is a number, just push it into stack, if it is not, take last two numbers and execute an operation on them, then push it again into stack.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for i in tokens:
            if i not in '-+*/':
                stack.append(int(i))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                if i == "+":
                    stack.append(v1 + v2)
                elif i == '-':
                    stack.append(v1 - v2)
                elif i == '/':
                    stack.append(int(v1 / v2))
                else:
                    stack.append(v1 * v2)
        return stack[0]