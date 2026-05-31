# Beautiful Triplets

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Easy
- Problem ID: 20732
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/beautiful-triplets/problem](https://www.hackerrank.com/challenges/beautiful-triplets/problem)

## Problem

Given a sequence of integers $a$, a triplet $(a[i],a[j],a[k])$ is beautiful if:

* $i<j<k$
* $a[j]-a[i] = a[k]-a[j] = d$

Given an increasing sequenc of integers and the value of $d$, count the number of beautiful triplets in the sequence.

**Example**   
$arr = [2, 2, 3, 4, 5]$   
$d = 1$    

There are three beautiful triplets, by index: $[i,j,k] = [0,2,3],[1,2,3],[2,3,4]$.  To test the first triplet, $arr[j] - arr[i] = 3 - 2 = 1$ and $arr[k] - arr[j] = 4 - 3 = 1$.  

**Function Description**  

Complete the *beautifulTriplets* function in the editor below.     

beautifulTriplets has the following parameters:  

- *int d:* the value to match   
- *int arr[n]:*  the sequence, sorted ascending   

**Returns**   

- *int:* the number of beautiful triplets

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 11/11 passed |
| Submission ID | 473403422 |

---

_Synced with AlgorithmHub_