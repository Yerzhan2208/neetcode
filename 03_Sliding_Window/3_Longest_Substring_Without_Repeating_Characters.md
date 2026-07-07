---
id: "3"
title: Longest Substring Without Repeating Characters
difficulty: 🟡 Medium
pattern: Sliding Window
leetcode_url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
status: 🟨 Reviewing
time_complexity: O(n) - n is the length of string
space_complexity: O(m) - m is the number of unique elements
date_created: 2026-07-07
---

## 🎯 Core Intuition
My solution is for each character, I iterate through other consequent characters until I found the duplicate one (can check it with the hash set), then if there is the duplicate, calculate its length and remove the first character. Therefore, we advance through the string and the second iterator starts from where it stopped (all characters before are already unique). Thus, by saving the maximum length, we can output the result


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        lc = 0
        res = 0
        ss = set()
        for i in range(len(s)):
            ss.add(s[i])
            for j in range(lc, len(s)):
                if j == i:
                    continue
                if s[j] not in ss:
                    ss.add(s[j])
                    continue
                else:
                    lc = j
                    break
            res = max(res, len(ss))
            ss.remove(s[i])
        return res