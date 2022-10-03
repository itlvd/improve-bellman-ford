# An Improved Bellman-Ford

## Algorithms 
This is consists of 4 versions of shortest path algorithms:
- Original Bellman - Ford.
- Early terminate Bellman - Ford.
- Yen's algorithm combines early terminate.
- Randomized algorithm based on Yen's algorithm.

## Data
### Data Type
I save the data with edge in text file, does not the adj matrix. The input data look like: `u->v=w`
- `u` from vertex
- `v` destination vertex
- `w` weight of edge `u->v`

But you can customize the data for your purpose. I used the format `u->v=w` because it's easy to present to another to understand and don't mistake.

In the program, data save with `[[u1,v1,w1],[u2,v2,w2],...]`

### Generate graph
The code generate graph based on NetworkX:
- Firstly, I generate undirected graph.
- Next, I choose a direct `u->v` or `u<-v` with variable probability.
- Then, I random the weight `w` of edge `u->v` or `u<-v`.
- Lastly, I export to data text file with format `u->v=w`.

## How to run
### Data Generate
You see the variable in Generate_graph.ipynb:
```python
num_node = 2000         # Number of nodes
p = 0.5                 # Probability `u->v` in a directed graph 
lenfrom = 1             # Number starts in weight `w` 
lenend = 10             # End number in the weight `w`
negative = False        # If `negative = False`, then a range of w randomized the weight is in [lenfrom,lenend]. Else, it is in [-lenend,lenend].
wantdraw = False        # Selecting `True`, if you want to plot the undirected graph.
```
### Algorithms
#### Variable
You can find the variable in algorithm python file:
```python
#============= Setup variable =======================
begin = 0
end = 199
path_data = "./data_demo/200node.txt" # path your data file.
print_shortest_path = True;           # print shortest path from `begin` to `end`
print_all_solution = False;           # print shortest path from `begin` to all vertex.
#====================================================
```
If your data does not a number, like `a->b=3`. You must to change variable to string `begin = 'a'`
#### Function
```python
print_solution(P,D,Point)              # Printing all shortest path from start vertex to another vertex.
printPath(start,des,P,D,Point)         # Printing shortest path from start vertex to destination vertex which you setup above.
```

# Evaluation

To be objective, the test did not run different programs during the test. I tried running three times. Results ± 20 seconds and then averaged.

**Machine**
- Core i5 - 4570 @ 3.20 Hz (4 CPUs).
- Ram: 16GB.
- Windows 11 Pro.
- Main H81 Gigabyte.

**Metric**: time to run (seconds)

| Data (Nodes - Edges) |        Bell       |      Terminate      |        Yen        |       Random      |
|:--------------------:|:-----------------:|:-------------------:|:-----------------:|:-----------------:|
|       50 - 529       |       0.092       |        0.086        |       0.096       |       0.091       |
|      200 - 8952      |       0.842       |        0.359        |       0.536       |       0.620       |
|      2000 ~ 1 M      | 895.411  ~ 14 min | 332.254  ~ 5 m 30 s | 295.318 ~ 4 m 54s | 345.726 ~ 5 m 45s |

## License
[MIT License](https://github.com/itlvd/improve-bellman-ford/blob/main/LICENSE)

## Reference
[Randomized Speedup of the Bellman-Ford Algorithm](https://arxiv.org/abs/1111.5414)
