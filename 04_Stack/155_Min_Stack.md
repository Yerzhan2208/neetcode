---
id: "155"
title: Min Stack
difficulty: 🟡 Medium
pattern: Stack
leetcode_url: https://leetcode.com/problems/min-stack/description/
status: 🟨 Reviewing
time_complexity: O(1) - operations
space_complexity: O(n) - length of stack
date_created: 2026-07-17
---

## 🎯 Core Intuition
The solution is simple for all the operations except the return min operation. The easiest way is just to call function min() to the array, however this is not the optimal solution. The optimal one would be to always track the minimum number, however if we removing the values, it becomes tricky.


## 🚀 Optimal Solution

### Python Implementation
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = 100000
        self.l = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.l += 1

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop(-1)
        self.l -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
```