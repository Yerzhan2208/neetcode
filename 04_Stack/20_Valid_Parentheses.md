---
id: "20"
title: Valid Parentheses
difficulty: 🟢 Easy
pattern: Stack
leetcode_url: https://leetcode.com/problems/valid-parentheses/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of string
space_complexity: O(n) - length of stack
date_created: 2026-07-17
---

## 🎯 Core Intuition
We can review each character in the string and add it to the stack, if there is a valid parentheses, we remove them. This way, if the stack is empty, the result is valid, if there are some elements, it is not valid.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in "[{(":
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i == "]" and stack[-1] == '[':
                    stack.pop(-1)
                elif i == "}" and stack[-1] == '{':
                    stack.pop(-1)
                elif i == ")" and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False

        return stack == []