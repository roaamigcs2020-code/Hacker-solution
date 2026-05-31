# Caesar Cipher

> Algorithms | Strings | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Strings
- Difficulty: Easy
- Problem ID: 8640
- Max Score: 15
- Problem Link: [https://www.hackerrank.com/challenges/caesar-cipher-1/problem](https://www.hackerrank.com/challenges/caesar-cipher-1/problem)

## Problem

Julius Caesar protected his confidential information by encrypting it using a cipher. [Caesar's cipher](https://en.wikipedia.org/wiki/Caesar_cipher) shifts each letter by a number of letters.  If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.  In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

```xml
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
```

**Example**  
$s = \texttt{There's-a-starman-waiting-in-the-sky}$  
$k = 3$  

The alphabet is rotated by $3$, matching the mapping above.  The encrypted string is $\texttt{Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb}$.  

**Note:** The cipher *only* encrypts letters; symbols, such as `-`, remain unencrypted.	 

**Function Description**  

Complete the *caesarCipher* function in the editor below.  

caesarCipher has the following parameter(s):

- *string s*: cleartext  
- *int k*: the alphabet rotation factor  

**Returns**  

- *string:*  the encrypted string

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 15.0 |
| Testcases | 12/12 passed |
| Submission ID | 473403497 |

---

_Synced with AlgorithmHub_