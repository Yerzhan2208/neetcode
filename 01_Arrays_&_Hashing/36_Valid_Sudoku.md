---
id: "36"
title: Valid Sudoku
difficulty: 🟡 Medium
pattern: Hash Map
leetcode_url: https://leetcode.com/problems/valid-sudoku/description/
status: 🟩 Mastered
time_complexity: O(n * n) - n is the number of rows and columns to iterate
space_complexity: O(n) - n is the size of all required hash maps
date_created: 2026-07-02
---

## 🎯 Core Intuition
I was thinking of how to divide the columns rows and squares, then found out that I can use tuples as the dictionary keys. So for each cell (i // 3, j // 3) will decide the square, i - row, j - column. At first I realized this solution with only one dictionary, which caused incorrect filling of cells because i and j went to the same set. Then, I divided the dictionary into three and this solution worked


## 🚀 Optimal Solution

### Python Implementation
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        rows = defaultdict(set)
        columns = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in squares[(i // 3, j // 3)]:
                    return False
                if num in rows[i]:
                    return False          
                if num in columns[j]:
                    return False
                squares[(i // 3, j // 3)].add(num)
                rows[(i)].add(num)
                columns[(j)].add(num)
        return True