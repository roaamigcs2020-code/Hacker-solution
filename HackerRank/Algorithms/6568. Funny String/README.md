# Funny String

> Algorithms | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Strings
- Difficulty: Easy
- Problem ID: 6568
- Max Score: 25
- Problem Link: [https://www.hackerrank.com/challenges/funny-string/problem](https://www.hackerrank.com/challenges/funny-string/problem)

## Problem

In this challenge, you will determine whether a string is *funny* or not.  To determine whether a string is funny, create a copy of the string in reverse e.g. $abc \rightarrow cba$.  Iterating through each string, compare the absolute difference in the [ascii](https://en.wikipedia.org/wiki/ASCII) values of the characters at positions 0 and 1, 1 and 2 and so on to the end.  If the list of absolute differences is the same for both strings, they are funny.

Determine whether a give string is funny.  If it is, return `Funny`, otherwise return `Not Funny`.

**Example**  
$s = \texttt{'lmnop'}$  

The ordinal values of the charcters are $[108, 109, 110, 111, 112]$.  $s_{reverse} = \texttt{'ponml'}$ and the ordinals are $[112, 111, 110, 109, 108]$.  The absolute differences of the adjacent elements for both strings are $[1, 1, 1, 1]$, so the answer is `Funny`.

**Function Description**

Complete the *funnyString* function in the editor below.   

funnyString has the following parameter(s):  

- *string s:* a string to test  

**Returns**  

- *string:* either `Funny` or `Not Funny`

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 25.0 |
| Testcases | 10/10 passed |
| Submission ID | 473403541 |

---

_Synced with AlgorithmHub_