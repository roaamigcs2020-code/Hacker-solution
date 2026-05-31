# Jumping on the Clouds: Revisited

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Easy
- Problem ID: 21277
- Max Score: 15
- Problem Link: [https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem](https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem)

## Problem

A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be *thunderheads* or *cumulus* clouds.  The character must jump from cloud to cloud until it reaches the start again.  
  
There is an array of clouds, $c$ and an energy level $e = 100$. The character starts from $c[0]$ and uses $1$ unit of energy to make a jump of size $k$ to cloud $c[\textit{(i + k) % n}]$. If it lands on a thundercloud, $c[i] = 1$, its energy ($e$) decreases by $2$ additional units. The game ends when the character lands back on cloud $0$.
  
Given the values of $n$, $k$, and the configuration of the clouds as an array $c$, determine the final value of $e$ after the game ends.
  
**Example**. 
$c = [0, 0, 1, 0]$   
$k = 2$  

The indices of the path are $0 \to 2 \to 0$.  The energy level reduces by $1$ for each jump to $98$.  The character landed on one thunderhead at an additional cost of $2$ energy units.  The final energy level is $96$.
  
**Note:** Recall that $\textit{%}$ refers to the [modulo operation](https://en.wikipedia.org/wiki/Modulo_operation).  In this case, it serves to make the route circular.  If the character is at $c[n-1]$ and jumps $1$, it will arrive at $c[0]$.  

**Function Description**  

Complete the *jumpingOnClouds* function in the editor below.    

jumpingOnClouds has the following parameter(s):  

- *int c[n]:* the cloud types along the path  
- *int k:* the length of one jump  

**Returns**  

- *int:* the energy level remaining.

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 15.0 |
| Testcases | 9/9 passed |
| Submission ID | 473402087 |

---

_Synced with AlgorithmHub_