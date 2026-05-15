# Development Log – The Torchbearer

**Student Name:** Rithish Sivaraj  
**Student ID:** 828614313



---

## Entry 1 – 05/14: Initial Plan


_I have already answered the problem analysis part. Since that doesn't really require any code. I will most probably first precompute the shortest distances between 
the nodes using Dijikstras algorithm as described by the steps. I think the recursive search and figuring out the pruning logic will be the hardest task to do in this assignment. 
This is because we have to traverse many different orders of visitation for the nodes, while still managing efficiency, so pruning the branches without taking out the optimal solution might prove 
to be a bit of a problem. Aside from this, I am going to make my first commit, which contains my answers to the problem analysis, and the same answers printing for the explain_problem() function 
in torchbearer.py._

---

## Entry 2 – 05/14: Part 2: Precomputation Design



_I just completed the README portion and the coding portion for part 2. I came upon a wrongful assumption on this section. 
Initially, I assumed that the exit node also needed to be added to the list of sources, and wrote my code as such, appending the exit node to the sources. 
However, while filling out the table, and going through the other functions before writing, I found that we only need the distance TO the exit and 
not the distance FROM the exit. My responses and code reflect that now. Aside from this, I used the graph1 from the test on the bottom of the file and ran a quick test. 
I will be making my second commit now._

---

## Entry 3 – 05/14: Part 3: Algorithm Correctness

_Finished my responses for the three parts in algorithm correctness. Also updated torchbearer.py with the return for those answers. I am now going to make another commit, but I will add a few more entry spots onto the dev log for future entries._

---
## Entry 4 – 05/14: Part 4: Search Design



_Completed my responses for part 4 of the assignment. I updated torchbearer.py with the return of those responses to reflect. Will be commiting again now._

---
## Entry 5 – 05/14: Part 5 & 6 and Solve():



_Completed implementing the functions from part 5 and 6, and also completed solve(). I ran into a few bugs due to syntax but fixed them all and passing all the tests now. I also finished the README portion of 5 and still need to complete 6. I will be making another commit now._

---
## Entry 6 – 05/14: Part 6: Pruning README.md Completed



_Completed the README.md for part 6 and also added my references. Removed the additional instruction blocks. Filled out the time estimate, but it might be slightly off since I didn't really calculate the time correctly._

---

## Entry 7 – 05/14: Post-Implementation Reflection



_I have now completed the full implementation. After completion, I have better understood how we can use recursive searches and also shortest path preprocessing. Given more time I would maybe try to improve the recursive search since the visitation order number will grow extremely large when more relics get added by maybe enforcing earlier elimination of routes that aren't possible or perhaps a tighter pruning system._

---

## Final Entry – [Date]: Time Estimate


| Part | Estimated Hours |
|---|-----------------|
| Part 1: Problem Analysis | 0.7             |
| Part 2: Precomputation Design | 1.5             |
| Part 3: Algorithm Correctness | 0.75            |
| Part 4: Search Design | 0.5             |
| Part 5: State and Search Space | 1               |
| Part 6: Pruning | 1               |
| Part 7: Implementation | 1               |
| README and DEVLOG writing | 0.75            |
| **Total** | 6.2             |
