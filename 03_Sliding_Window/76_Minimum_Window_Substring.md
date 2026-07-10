---
id: "76"
title: Minimum Window Substring
difficulty: 🔴 Hard / 🟡 Medium / 🟢 Easy
pattern: Hash Map & Sliding Window
leetcode_url: https://leetcode.com/problems/minimum-window-substring/description/
status: 🟨 Reviewing
time_complexity: O(n) - length of array
space_complexity: O(m) - m is the number of unique elements
date_created: 2026-07-10
---

## 🎯 Core Intuition
I was not able to solve this question for the first time, so I have walked through the solution. My tries were close to the solution, but the aha-moment was the counting need and have values, so it will be able to identify if the substring contains the characters from the t. we simply move the right pointer and look if we have all the needed characters, if we have, we move the left pointer and save the result in res and resLen. then we decrease have if the value where left pointer is is removed from the window. So, now we again didn't have the needed chars, so we continue to iterate r until again have == need. The intuition behind this problem is simple, however solution is tricky.


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("infinity")
        have = 0
        need = len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
```

