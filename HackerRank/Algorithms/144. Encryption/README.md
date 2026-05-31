# Encryption

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Medium
- Problem ID: 144
- Max Score: 30
- Problem Link: [https://www.hackerrank.com/challenges/encryption/problem](https://www.hackerrank.com/challenges/encryption/problem)

## Problem

An English text needs to be encrypted using the following encryption scheme.  
First, the spaces are removed from the text. Let $L$ be the length of this text.  
Then, characters are written into a grid, whose rows and columns have the following constraints:

$$\lfloor\sqrt{L}\rfloor \le row \le column \le \lceil\sqrt{L}\rceil\text{, where }\lfloor x \rfloor \text{ is floor function and }\lceil x \rceil\text{ is ceil function}$$ 
 
**Example**  

$s = \texttt{if man was meant to stay on the ground god would have given us roots}$  

After removing spaces, the string is $54$ characters long.  $\sqrt{54}$ is between $7$ and $8$, so it is written in the form of a grid with 7 rows and 8 columns. 

    ifmanwas  
    meanttos          
    tayonthe  
    groundgo  
    dwouldha  
    vegivenu  
    sroots

+ Ensure that $rows \times columns \ge L$   
+ If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. $rows \times columns$.  

The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded message for the grid above is:  
    
`imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau`  
    
Create a function to encode a message.

**Function Description**  

Complete the *encryption* function in the editor below.  

encryption has the following parameter(s):  

- *string s:* a string to encrypt  

**Returns**  

- *string:* the encrypted string

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 30.0 |
| Testcases | 13/13 passed |
| Submission ID | 473403405 |

---

_Synced with AlgorithmHub_