---
id: "4"
title: Median of Two Sorted Arrays
difficulty: 🔴 Hard
pattern: Binary Search/Two Pointers/Array
leetcode_url: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
status: 🟨 Reviewing
time_complexity: O(n + m) - my solution; O(log(min(n, m)) - optimal solution
space_complexity: O(n + m) - my solution, creating an array; O(1) - optimal solution
date_created: 2026-07-18
---

## 🎯 Core Intuition
My first intuition was trivial solution, by just combining the arrays, sorting, and finding the median. However, it is the least optimal solution. The approach I tried is just to check all the numbers in both arrays and combine them in increasing order until total length // 2. So, this way the average of the last two elements will be the median, or the last element itself.

## 🚀 My Solution

### Python Implementation
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        l = 0
        r = 0
        totalLength = len(nums1) + len(nums2)
        count = (totalLength // 2) + 1

        while count > 0:
            if l == len(nums1):
                while count > 0 and r != len(nums2):
                    nums.append(nums2[r])
                    r += 1
                    count -= 1
                break
            elif r == len(nums2):
                while count > 0 and l != len(nums1):
                    nums.append(nums1[l])
                    l += 1
                    count -= 1
                break

            if nums1[l] < nums2[r]:
                nums.append(nums1[l])
                l += 1
            else:
                nums.append(nums2[r])
                r += 1
            count -= 1
        return (nums[-1]) if totalLength % 2 == 1 else (nums[-1] + nums[-2]) / 2
```
## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
```