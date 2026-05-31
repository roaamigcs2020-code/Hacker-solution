# String Construction 

> Algorithms | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Strings
- Difficulty: Easy
- Problem ID: 21584
- Max Score: 25
- Problem Link: [https://www.hackerrank.com/challenges/string-construction/problem](https://www.hackerrank.com/challenges/string-construction/problem)

## Problem

Amanda has a string of lowercase letters that she wants to copy to a new string.  She can perform the following operations with the given costs. She can perform them any number of times to construct a new string $p$:

* Append a character to the end of string $p$ at a cost of $1$ dollar. 
* Choose any [substring](https://en.wikipedia.org/wiki/Substring) of $p$ and append it to the end of $p$ at no charge.

Given $n$ strings $s[i]$, find and print the *minimum* cost of copying each $s[i]$ to $p[i]$ on a new line.

For example, given a string $s = abcabc$, it can be copied for $3$ dollars.  Start by copying $a$, $b$ and $c$ individually at a cost of $1$ dollar per character.  String $p = abc$ at this time.  Copy $p[0:2]$ to the end of $p$ at no cost to complete the copy.  

**Function Description**  

Complete the *stringConstruction* function in the editor below.  It should return the minimum cost of copying a string.  

stringConstruction has the following parameter(s):  

- *s*: a string

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 25.0 |
| Testcases | 13/13 passed |
| Submission ID | 473403735 |

---

_Synced with AlgorithmHub_