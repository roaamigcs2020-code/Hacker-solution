# Jumping on the Clouds

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Easy
- Problem ID: 20832
- Max Score: 20
- Problem Link: [https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem)

## Problem

There is a new mobile game that starts with consecutively numbered clouds.  Some of the clouds are thunderheads and others are cumulus.  The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus $1$ or $2$.  The player must avoid the thunderheads.  Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.  It is always possible to win the game.  

For each game, you will get an array of clouds numbered $0$ if they are safe or $1$ if they must be avoided.  

**Example**  
$c = [0,1,0,0,0,1,0]$  

Index the array from $0\ldots 6$.  The number on each cloud is its index in the list so the player must avoid the clouds at indices $1$ and $5$.  They could follow these two paths: $0 \to 2 \to 4 \to 6$ or $0 \to 2 \to 3 \to 4 \to 6$.  The first path takes $3$ jumps while the second takes $4$.  Return $3$.

**Function Description**  

Complete the *jumpingOnClouds* function in the editor below.  

jumpingOnClouds has the following parameter(s):  

- *int c[n]*: an array of binary integers  

**Returns**  

- *int:* the minimum number of jumps required

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 20.0 |
| Testcases | 9/9 passed |
| Submission ID | 473403368 |

---

_Synced with AlgorithmHub_