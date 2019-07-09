# hackerRank
Code for Array Manipulation problem of www.hackerrank.com

https://www.hackerrank.com/challenges/crush/problem

In src/hard/ there is a solution with Linked Lists and BST to store intervals like single numbers, that is to say in each node there is a number; the BST is introduced to make the search faster. This solution is correct but isn't performant enough.

In src/extreme/ there is a solution with Interval Trees, a data structure that comes augmenting Red-Black Trees; the idea on how to solve the problem with Interval Trees is to have disjointed intervals, so that the Interval_Search function, ran repeatedly, finds all the overlapping intervals, and not just one. Anyway, this brings to a lot of nodes, and so the performance gain is lost; plus, test n°4 doesn't match.
