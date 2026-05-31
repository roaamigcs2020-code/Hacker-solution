# Happy Ladybugs

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Easy
- Problem ID: 21763
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/happy-ladybugs/problem](https://www.hackerrank.com/challenges/happy-ladybugs/problem)

## Problem

Happy Ladybugs is a board game having the following properties:

* The board is represented by a string, $b$, of length $n$. The $i^{th}$ character of the string, $b[i]$, denotes the $i^{th}$ cell of the board.
    * If $b[i]$ is an underscore (i.e., `_`), it means the $i^{th}$ cell of the board is empty.
    * If $b[i]$ is an uppercase English alphabetic letter (ascii[A-Z]), it means the $i^{th}$ cell contains a ladybug of color $b[i]$.
    * String $b$ will not contain any other characters.
- A ladybug is *happy* only when its left or right adjacent cell (i.e., $b[i \pm 1]$) is occupied by another ladybug having the same color.
- In a single move, you can move a ladybug from its current position to any empty cell. 
<br>

Given the values of $n$ and $b$ for $g$ games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, return `YES` if all the ladybugs can be made happy through some number of moves.  Otherwise, return `NO`.      
**Example**     
$b=[YYR\_B\_BR]$    

You can move the rightmost $B$ and $R$ to make $b=[YYRRBB\_\_]$ and all the ladybugs are happy. Return `YES`.   

**Function Description**  

Complete the *happyLadybugs* function in the editor below.   

happyLadybugs has the following parameters:

- *string b:* the initial positions and colors of the ladybugs   

**Returns**   

- *string:* either `YES` or `NO`

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 12/12 passed |
| Submission ID | 473403432 |

---

_Synced with AlgorithmHub_