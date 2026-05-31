# Organizing Containers of Balls

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Medium
- Problem ID: 32644
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem](https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem)

## Problem

David has several containers, each with a number of balls in it.  He has just enough containers to sort each type of ball he has into its own container.  David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

* Each container contains only balls of the same type.
* No two balls of the same type are located in different containers.


**Example**   

$containers = [[1, 4], [2, 3]]$   

David has $n=2$ containers and $2$ different types of balls, both of which are numbered from $0$ to $n-1 = 1$. The distribution of ball types per container are shown in the following diagram.   

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485811368-9e78c98652-swapping-balls.png)

In a single operation, David can *swap* two balls located in different containers.

The diagram below depicts a single swap operation:

![image](https://s3.amazonaws.com/hr-challenge-images/0/1485811849-e97b84e218-swapping-balls-ps-1.png)

In this case, there is no way to have all green balls in one container and all red in the other using only swap operations.  Return `Impossible`.  

You must perform $q$ queries where each query is in the form of a matrix, $M$. For each query, print ``Possible`` on a new line if David can satisfy the conditions above for the given matrix.  Otherwise, print ``Impossible``.  

**Function Description**  

Complete the *organizingContainers* function in the editor below.   

organizingContainers has the following parameter(s):  

- *int containter[n][m]*: a two dimensional array of integers that represent the number of balls of each color in each container  

**Returns**   

- *string:*  either `Possible` or `Impossible`

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 7/7 passed |
| Submission ID | 473403399 |

---

_Synced with AlgorithmHub_