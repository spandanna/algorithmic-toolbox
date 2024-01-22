# Initial examples
- Find maximum number from an array of numbers e.g. [1,5,2,9,0] => 95210
- Optimal queue arrangement t1 = 15, t2 = 20, t3=10 => 3,1,2

# Greedy Strategy
- Make a greedy choice (e.g. max, min, avg)
- Reduce to smaller problem - sub problem (e.g. remove)
- Iterate (e.g. repeat on remaining)

# Safe choice
- Greedy choice is safe choice is there is an optimal solution consistent with the first choice (first time it's reduced to sub problem).
- e.g. when t2 > t1 (above) it is optimal for t1 to go first. This means total waiting time is 15 mins (t1) rather than 20 mins (t2)

# Implementation
- Nested for loop (for each patient in queue, find the minimum waiting time (by looping through patients) and treat) O(n^2)
- If patients are sorted first O(logn), it can be reduced to O(nlogn)

# Celebration party problem
- Creating minimum number of similar age (max diff 2 years) groups of children
- Naive algorithm: try all possible combinations of children in one or more groups, check each distribution for max age difference and return minimum number of groups among valid distributions - at least 2^n

# Covering points by segments
- Minimum number of fixed segments to cover set of points
- For problem above, segment length is 2 years
- Safe choice: start first segment at leftmost point > then keep repeating this...

# Maximising loot
- 




