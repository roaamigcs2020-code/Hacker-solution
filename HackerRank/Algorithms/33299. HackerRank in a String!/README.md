# HackerRank in a String!

> Algorithms | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Strings
- Difficulty: Easy
- Problem ID: 33299
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem](https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem)

## Problem

We say that a string contains the word `hackerrank` if a [subsequence](https://en.wikipedia.org/wiki/Subsequence) of its characters spell the word `hackerrank`.  Remeber that a subsequence maintains the order of characters selected from a sequence.   

More formally, let $p[0], p[1], \cdots, p[9]$ be the respective indices of `h`, `a`, `c`, `k`, `e`, `r`, `r`, `a`, `n`, `k` in string $s$. If $p[0] < p[1] < p[2] < \cdots < p[9]$ is true, then $s$ contains `hackerrank`.

For each query, print `YES` on a new line if the string contains `hackerrank`, otherwise, print `NO`.  

**Example**  
$s=\text{haacckkerrannkk}$  

This contains a subsequence of all of the characters in the proper order.  Answer `YES`  

$s=\text{haacckkerannk}$  

This is missing the second 'r'.  Answer `NO`.  

$s = \text{hccaakkerrannkk}$  

There is no 'c' after the first occurrence of an 'a', so answer `NO`.  


**Function Description**  

Complete the *hackerrankInString* function in the editor below.   

hackerrankInString has the following parameter(s):  

- *string s:* a string   

**Returns**  

- *string:* `YES` or `NO`

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 4/4 passed |
| Submission ID | 473403516 |

---

_Synced with AlgorithmHub_