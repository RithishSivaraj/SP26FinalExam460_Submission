# Development Log – The Torchbearer

**Student Name:** Rithish Sivaraj  
**Student ID:** 828614313

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – 05/14: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_I have already answered the problem analysis part. Since that doesn't really require any code. I will most probably first precompute the shortest distances between 
the nodes using Dijikstras algorithm as described by the steps. I think the recursive search and figuring out the pruning logic will be the hardest task to do in this assignment. 
This is because we have to traverse many different orders of visitation for the nodes, while still managing efficiency, so pruning the branches without taking out the optimal solution might prove 
to be a bit of a problem. Aside from this, I am going to make my first commit, which contains my answers to the problem analysis, and the same answers printing for the explain_problem() function 
in torchbearer.py._

---

## Entry 2 – 05/14: Part 2: Precomputation Design

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_I just completed the README portion and the coding portion for part 2. I came upon a wrongful assumption on this section. 
Initially, I assumed that the exit node also needed to be added to the list of sources, and wrote my code as such, appending the exit node to the sources. 
However, while filling out the table, and going through the other functions before writing, I found that we only need the distance TO the exit and 
not the distance FROM the exit. My responses and code reflect that now. Aside from this, I used the graph1 from the test on the bottom of the file and ran a quick test. 
I will be making my second commit now._

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|-----------------|
| Part 1: Problem Analysis | 0.7             |
| Part 2: Precomputation Design | 1.5             |
| Part 3: Algorithm Correctness |                 |
| Part 4: Search Design |                 |
| Part 5: State and Search Space |                 |
| Part 6: Pruning |                 |
| Part 7: Implementation |                 |
| README and DEVLOG writing |                 |
| **Total** |                 |
