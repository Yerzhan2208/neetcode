---
id: "853"
title: Car Fleet
difficulty: 🟡 Medium
pattern: Stack
leetcode_url: https://leetcode.com/problems/car-fleet/description/
status: 🟨 Reviewing
time_complexity: O(nlogn) - sorting
space_complexity: O(n) - length of stack
date_created: 2026-07-17
---

## 🎯 Core Intuition
The challenging part was to recognize that we need to sort array in decreasing order, then the problem becomes quite easy as we need only to calculate the time to target for each car. If the time of current car is less or equal to the car on the top, then it becomes the fleet, otherwise push the car into the stack. The result will be the length of the stack


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(position[i], speed[i]) for i in range(len(position))]
        ps.sort(reverse=True)
        stack = []

        for p, s in ps:
            time = (target - p) / s
            if stack:
                if time <= stack[-1]:
                    continue
            stack.append(time)
                    
        return len(stack)