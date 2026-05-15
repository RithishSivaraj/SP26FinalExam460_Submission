"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Rithish Sivaraj
Student ID:   828614313

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """

    return """
    Why a single shortest-path run from S is not enough:
    - The single shortest-path run from S only determines the cheapest cost from S to all the individual nodes.
    - Specifically, it doesn't make a decision on which of the chambers holding relics should be visited next, and what sequence it should follow for all the relics to be collected before exiting.

    What decision remains after all inter-location costs are known:
    - Finding the order the chambers with the relics should be visited before exiting, while still minimizing the fuel cost.

    Why this requires a search over orders (one sentence):
    - This is because the cost depends on the sequence that the chambers are all visited, so multiple orders need to be checked to find the path costing the least.
    """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    selected_sources = []       # storing all the nodes to be used in Dijkstra source nodes.
    if spawn not in selected_sources:
        selected_sources.append(spawn)      # adding the spawn node first

    r = 0
    while r < len(relics):      # looping through and adding all the relic nodes if it hasn't already been added.
        if relics[r] not in selected_sources:
            selected_sources.append(relics[r])
        r = r + 1

    return selected_sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    node_distances = {}     # creating empty dict to store the shortest distance between the spawn and the node
    for node in graph.keys():
        node_distances[node] = float('inf')     # setting all the node distances to inf, so they are unreachable until it is proven they are reachable.

    node_distances[source] = 0      # since distance from source to source is just 0
    pr_queue = []       # creating an empty priority queue
    heapq.heappush(pr_queue, (0, source))       # adding the source node ro the priority queue with its distance.
    while len(pr_queue) > 0:
        smallest_node = heapq.heappop(pr_queue)     # removing node with the shortest distance currently
        distance_current = smallest_node[0]
        node_current = smallest_node[1]         # seperated the tuple into distance and node.

        if distance_current > node_distances[node_current]:
            continue        # skipping if a better entry was found

        neighbor_nodes = graph[node_current]            # all the neighboring nodes which are reachable directly from the current node.
        for edge in neighbor_nodes:
            neighbor_node = edge[0]
            cost = edge[1]                      # getting the destination node and the cost of the edge.

            total_cost = distance_current + cost        # getting the total cost of getting to that neighboring node from the current node.

            if total_cost < node_distances[neighbor_node]:          # checking to see if the new path is cheaper.
                node_distances[neighbor_node] = total_cost
                heapq.heappush(pr_queue, (total_cost, neighbor_node))

    return node_distances

    # pass


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)      # selecting the nodes to run Dijkstras
    distance_table = {}                     # creating a nested dict to store the shortest path tables
    for s in sources:
        distance_table[s] = run_dijkstra(graph, s)      # running dijkstras one time from the selected source nodes.

    return distance_table
    # pass


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """
    What the Invariant Means:
    - For nodes already finalized (in S): These recorded distances are guaranteed to be the actual minimum distance possible. 
      From this point, it isn't possible to find a shorter distance than these recorded ones.

    - For nodes not yet finalized (not in S): The distances recorded here are currently the shortest path discovered, using 
    the nodes that are already finalized to go through as steps. But there is still a possibility that a cheaper or shorter 
    path exists going through nodes that haven't been finalized.
      
    Why Each Phase Holds:
    Initialization : why the invariant holds before iteration 1: Before even the first step executes, the source node 
    distance is 0 and all the nodes are set to inf. Also we haven't finalized any nodes yet, so the invariant holds.
    
    Maintenance : why finalizing the min-dist node is always correct: Finalizing the min-dist node is always correct 
    because this node will have the smallest distance tentatively, and since all the edge weights are non-negative. 
    This means that a later path with a smaller distance to that same node, can't be produced.

    Termination : what the invariant guarantees when the algorithm ends: When the algorithm finishes running, the heap 
    is empty and all the reachable nodes are already finalized with their actual shortest path from the source node. 
    Also, the nodes with inf still are unreachable.
    
    Why This Matters for the Route Planner:
    Ensuring that we have the correct distance, will allow the routing decisions to be made correctly by comparing the visitation 
    orders to choose the route with the least amount of fuel used, and having an incorrect ordering could produce a route that does 
    not minimize fuel cost.
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """
    -Why Greedy Fails
    The failure mode: The greedy algorithm will only choose the next shortest path to a relic, and doesn't account for how 
    that choice can cause the overall route to end up more expensive than need be.
    Counter-example setup: _Consider nodes A, B, C with spawn S and exit T, with costs: S -> A = 1, S -> B = 2, S -> C = 2, 
    A -> B = 100, A -> C = 100, B -> C = 1, C -> A = 1, and A -> T = 1.
    What greedy picks: S -> A -> B -> C -> T, which has a total cost of 103.
    What optimal picks: S -> B -> C -> A -> T, with a total cost of 5
    Why greedy loses: Greedy loses because by picking the choice which would procure the smallest cost now, it fails to 
    consider that it could be navigating to a more expensive choice later.
    
    What the Algorithm Must Explore
    The algorithm has to explore all the different orders of visitation between S to all the relics. This is because the total 
    cost depends on the entire sequence and not just the immediate next choice, and we want to minimize the total cost.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
