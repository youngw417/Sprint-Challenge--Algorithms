#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n)
the iteration will increate linearly with the increase of n


b) O(n^2)
for every iteration of outer loop, there is some number of inner loop iteration.  O(n * 1/2n) = O(1/2 * n^2) = O(n^2)

c) O(n)
for the increase of input value, there is the same increase of recursion calls.

## Exercise II

1. go the middle of the foor of building
2. throw the ege to see whether it breaks
3. if it breaks, then go to middle floor of lower half and throw egg.
4. else if it does not break, then go to middle floor of higher half and throw the egg.
5. keep doing this recursively until you find the middle floor floor at last from which you would break or does not break when you throw egg
6. if the egg break at last middle, the floor f is the one below
7. if the egg does not break at last middle, the follor f is the one

this Binary Search of log(n)