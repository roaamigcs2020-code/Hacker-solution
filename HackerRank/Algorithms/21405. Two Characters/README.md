# Two Characters

> Algorithms | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Strings
- Difficulty: Easy
- Problem ID: 21405
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/two-characters/problem](https://www.hackerrank.com/challenges/two-characters/problem)

## Problem

Given a string, remove characters until the string is made up of any two alternating characters.  When you choose a character to remove, all instances of that character must be removed.  Determine the longest string possible that contains just two alternating letters.

**Example**    

$s = \text{'abaacdabd'}$   

Delete `a`, to leave `bcdbd`.  Now, remove the character `c` to leave the valid string `bdbd` with a length of 4. Removing either `b` or `d` at any point would not result in a valid string.  Return $4$.   

Given a string $s$, convert it to the longest possible string $t$ made up only of alternating characters.  Return the length of string $t$.  If no string $t$ can be formed, return $0$.

**Function Description**

Complete the *alternate* function in the editor below.  

alternate has the following parameter(s):  

- *string s:* a string   

**Returns**. 

- *int:* the length of the longest valid string, or $0$ if there are none

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 33/33 passed |
| Submission ID | 473403480 |

---

_Synced with AlgorithmHub_