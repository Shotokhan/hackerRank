# hackerRank
Code for Array Manipulation problem of www.hackerrank.com

https://www.hackerrank.com/challenges/crush/problem

In src/hard/ there is a solution with Linked Lists and BST to store intervals like single numbers, that is to say in each node there is a number; the BST is introduced to make the search faster. This solution is correct but isn't performant enough.

In src/extreme/ there is a solution with Interval Trees, a data structure that comes augmenting Red-Black Trees; the idea on how to solve the problem with Interval Trees is to have disjointed intervals, so that the Interval_Search function, ran repeatedly, finds all the overlapping intervals, and not just one. Anyway, this brings to a lot of nodes, and so the performance gain is lost; plus, test n°4 doesn't match.

In src/differenceArray there is a solution hard to think, I saw it in this video: https://www.youtube.com/watch?v=hDhf04AJIRs&list=PLSIpQf0NbcCltzNFrOJkQ4J4AAjW3TSmA.

Since I didn't come to the difference array solution on my own, I think it was a good exercise about thinking on data structures, testing, debugging and profiling. This is also my first repo on GitHub.
