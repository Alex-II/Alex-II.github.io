---
layout: default
title: "PowerGraph: Distributed Graph-Parallel Computation on Natural Graphs [Talk]"
category: notes
---

# [PowerGraph: Distributed Graph-Parallel Computation on Natural Graphs](https://www.usenix.org/node/170825)

## Graphs are Ubiquitous
- Used by many major products e.g. Google, Netflix
- Gigantic (billions of vertices, edges)
- Used for ML, data mining

## <i>Natural Graphs</i> (having Power-Law Distribution)
- (Certain) Graph data follows power-law distribution 
    - Small set of vertices have high degree of connections
  
![powergraph_star_motif.PNG](/assets/powergraph_star_motif.PNG)
![powergraph_power_law_distribution](/assets/powergraph_power_law_distribution.PNG)
- Difficult to partition by partitioning vertices
  
## Classic Distributed Graph Approach:
- Evenly distribute **vertices** to different machines
    - Issue: High-degree vertices can't fit all edges on one machine (i.e. many edges are connected to a vertex on another machine)
- ![powergraph_partition_cuts](/assets/powergraph_classic_partition.PNG)


### Pregel Communication Overhead for Highly-Connected Vertex
- High-degree vertex incurs communication cost for its **outgoing messages** in Pregel systems
    - Despite all messages going to Machine 1 from Machine 2
![powergraph_fanout_overhead](/assets/powergraph_fanout_overhead.PNG)
- **Incoming messages** overhead mitigated by combining messages coming from the same machine

### GraphLab Communication Overhead for Highly-Connected Vertex
- GraphLab solves the **outgoing messages** by 'ghosting' a node to neighboring machines
    - One chance to D implies one single **outgoing** update
![powergraph_graphlab_ghosting](/assets/powergraph_graphlab_ghosting.PNG)
- **Incoming updates** however, still pose problems:
![powergraph_graphlab_incoming](/assets/powergraph_graphlab_incoming.PNG)


### Graph Partitioning: Cut Across Edges
- Vertices are assigned to machines and edges connect to neighboring vertices on other machines
    - Issue: Natural graphs cannot be partitioned with few inter-machine edges
![powergraph_cut_edges](/assets/powergraph_cut_edges.PNG)
    - Issue: Natural graphs will produce many *cut edges* (edge whose vertices are on different machines)


## PowerGraph
### New: Cut Across Vertices
![powergraph_cut_vertex](/assets/powergraph_cut_vertex.PNG)



### Workflow Observation
- Most workflows in 3 steps:
    1. Gather data from neighboring nodes
    2. Calculate a new value for own node
    3. Update neighboring nodes with new own value
- Named **GAS**:
    - (1) **G**ather (in parallel), (2) **A**pply (on own node), (3) **S**catter (in parallel)

### Distributed Execution
![powergraph_distributed_execution](/assets/powergraph_distributed_execution.PNG)

1. <u>Gather</u>: Machine 1,2,3 and 4 locally gather neighbor data for a local partial sum
2. <u>Gather</u>: Master Machine 1 receives the partial sums
3. <u>Gather</u>: Master Machine 1 sums all partial sums
4. <u> Apply</u>: Master Machine 1 updates local node and sends updates to Machines 2,3,4 so they update their local node
5. <u> Scatter </u>: Within each machine, new node info is communicated to on-machine neighbors 

### Communication Overhead
- Communication happens on vertex gather and apply
- No inter-machine communication occurs with edge information

### Edge Placements
- Partitioning must attempt to minimize how many machines a vertex spans (and thus must communicate with)
- Edges are assigned per machine, no vertices

#### Random
![powergraph_random_edge_placement](/assets/powergraph_random_edge_placement.PNG)
- Random is also fairly predictable, meaning simple understanding of needed resources

#### Coordinated Greedy
- Nodes coordinate to minimize how many machines a vertex spans
- (vs Random) requires coordination, slower to build
- (vs Random) lower communication overhead
- on placing an edge, heuristic tries to place it on:
  1. machine already containing both vertices of edge
  2. machine containing one vertex (tiebreaker: less loaded)
  3. no machine contains any vertices of the edge: assign to least loaded machine


#### Oblivious Greedy
- Middleground between Random and Coordinates: guesswork and little coordination between machines.

### Execution Modes

### Delta Caching

## Performance

### PowerGraph Placement: Random vs Coordinated vs Oblivious 
![powergraph_placement_compare](/assets/powergraph_placement_compare.PNG)
 

### PowerGraph vs Other Systems
![powergraph_perf_1](/assets/powergraph_perf_1.PNG)

![powergraph_perf_3](/assets/powergraph_perf_3.PNG)

![powergraph_perf_2](/assets/powergraph_perf_2.PNG)




