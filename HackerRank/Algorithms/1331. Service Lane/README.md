# Service Lane

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Easy
- Problem ID: 1331
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/service-lane/problem](https://www.hackerrank.com/challenges/service-lane/problem)

## Problem

A driver is driving on the freeway. The check engine light of his vehicle is on, and the driver wants to get service immediately. Luckily, a service lane runs parallel to the highway. It varies in width along its length.

![Paradise Highway](https://hr-testcases.s3.amazonaws.com/1331)

You will be given an array of widths at points along the road (*indices*), then a list of the indices of entry and exit points. Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely.

**Example**    
$n = 4$   
$width = [2,3,2,1]$   
$cases = [[1, 2], [2, 4]]$  

If the entry index, $i = 1$ and the exit, $j = 2$, there are two segment widths of $2$ and $3$ respectively.  The widest vehicle that can fit through both is $2$.  If $i = 2$ and $j = 4$, the widths are $[3,2,1]$ which limits vehicle width to $1$.  

**Function Description**  

Complete the *serviceLane* function in the editor below.  

serviceLane has the following parameter(s):  

- *int n:* the size of the $width$ array  
- *int cases[t][2]:* each element contains the starting and ending indices for a segment to consider, inclusive    

**Returns**  

- *int[t]:* the maximum width vehicle that can pass through each segment of the service lane described

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 12/12 passed |
| Submission ID | 473403444 |

---

_Synced with AlgorithmHub_