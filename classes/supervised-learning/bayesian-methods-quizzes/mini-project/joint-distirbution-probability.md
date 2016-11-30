## If you wanted to measure the joint probability distribution of a missing word given its position relative to every other word in the document, how many probabilities would you need to measure? Say the document is N words long. 

- Number of words: `N`
- Number of possible missing word's positions (i.e: first word missing, second word missing, etc.): `N`
- Number of possible distances between missing word and the other words. For each possible position, we have `N` other words, so the final answer is: `N^2`