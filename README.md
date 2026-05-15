# The Torchbearer

**Student Name:** Rithish Sivaraj   
**Student ID:** 828614313   
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis



- **Why a single shortest-path run from S is not enough:**
  * The single shortest-path run from S only determines the cheapest cost from S to all the individual nodes.
  * Specifically, it doesn't make a decision on which of the chambers holding relics should be visited next, and what sequence it should follow for all the relics to be collected before exiting.

- **What decision remains after all inter-location costs are known:**
  * Finding the order the chambers with the relics should be visited before exiting, while still minimizing the fuel cost.

- **Why this requires a search over orders (one sentence):**
  * This is because the cost depends on the sequence that the chambers are all visited, so multiple orders need to be checked to find the path costing the least.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source                                                                                                |
|------------------|-------------------------------------------------------------------------------------------------------------------|
| _spawn_          | All the paths will start from S or the spawn from torchbearer.py.                                                 |
| _relics_         | After getting to each relic, the search has to find the lowest costing path either to the next relic or the exit. |

### Part 2b: Distance Storage


| Property | Your answer                                                                                    |
|---|------------------------------------------------------------------------------------------------|
| Data structure name | nested dictionary (a dictionary within a dictionary).                                          |
| What the keys represent | The inner keys represent the destination nodes, while the outer keys represent source nodes.   |
| What the values represent | The smallest amount fuel will cost from the source node to the destination node.               |
| Lookup time complexity | O(1)                                                                                           |
| Why O(1) lookup is possible | Python dictionaries use hash tables, so this allows lookups to be direct, and therefore, O(1). |

### Part 2c: Precomputation Complexity


- **Number of Dijkstra runs:** _for r number of relics, it would be r + 1_
- **Cost per run:** _O(m log n)_
- **Total complexity:** _O((r + 1) * m log n)_
- **Justification (one line):** _You have to run Dijkstra once on the spawn node, and then an aditional run on each of the relic nodes._

---

## Part 3: Algorithm Correctness


### Part 3a: What the Invariant Means


- **For nodes already finalized (in S):**
  _These recorded distances are guaranteed to be the actual minimum distance possible. From this point, it isn't possible to find a shorter distance than these recorded ones._

- **For nodes not yet finalized (not in S):**
  _The distances recorded here are currently the shortest path discovered, using the nodes that are already finalized to go through as steps. But there is still a possibility that a cheaper or shorter path exists going through nodes that haven't been finalized._

### Part 3b: Why Each Phase Holds


- **Initialization : why the invariant holds before iteration 1:**
  _Before even the first step executes, the source node distance is 0 and all the nodes are set to inf. Also we haven't finalized any nodes yet, so the invariant holds._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Finalizing the min-dist node is always correct because this node will have the smallest distance tentatively, and since all the edge weights are non-negative. This means that a later path with a smaller distance to that same node, can't be produced._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _When the algorithm finishes running, the heap is empty and all the reachable nodes are already finalized with their actual shortest path from the source node. Also, the nodes with inf still are unreachable._

### Part 3c: Why This Matters for the Route Planner


_Ensuring that we have the correct distance, will allow the routing decisions to be made correctly by comparing the visitation orders to choose the route with the least amount of fuel used, 
and having an incorrect ordering could produce a route that does not minimize fuel cost._

---

## Part 4: Search Design

### Why Greedy Fails


- **The failure mode:** _The greedy algorithm will only choose the next shortest path to a relic, and doesn't account for how that choice can cause the overall route to end up more expensive than need be._
- **Counter-example setup:** _Consider nodes A, B, C with spawn S and exit T, with costs: S -> A = 1, S -> B = 2, S -> C = 2, A -> B = 100, A -> C = 100, B -> C = 1, C -> A = 1, and A -> T = 1.
- **What greedy picks:** _S -> A -> B -> C -> T, which has a total cost of 103._
- **What optimal picks:** _S -> B -> C -> A -> T, with a total cost of 5_
- **Why greedy loses:** _Greedy loses because by picking the choice which would procure the smallest cost now, it fails to consider that it could be navigating to a more expensive choice later._

### What the Algorithm Must Explore


- _The algorithm has to explore all the different orders of visitation between S to all the relics. This is because the total cost depends on the entire sequence and not just the immediate next choice, and we want to minimize the total cost._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type  | Description                                             |
|---|-----------------------|------------|---------------------------------------------------------|
| Current location | current_loc           | node       | Describes the node the current search is positioned at. |
| Relics already collected | relics_visited_order  | list[node] | stores the order of the relics being visited till now.  |
| Fuel cost so far | cost_so_far           | float      | current total of the fuel cost on the current path.     |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer                                                                                                                      |
|---|----------------------------------------------------------------------------------------------------------------------------------|
| Data structure chosen | set                                                                                                                              |
| Operation: check if relic already collected | Time complexity: O(1)                                                                                                            |
| Operation: mark a relic as collected | Time complexity:   O(1)                                                                                                          |
| Operation: unmark a relic (backtrack) | Time complexity:    O(1)                                                                                                         |
| Why this structure fits | The python set will allow existence checks to be run faster, and is more efficient to add or remove operations during recursion. |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _k!_
- **Why:** _In the worst case, we may need to go through every single order of relic visitation possible._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
