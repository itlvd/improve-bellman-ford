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
#============= Setup variable
begin = 0 # Start vertex.
end = 199 # Destination vertex.
#=============
```
If your data does not a number, like `a->b=3`. You must to change variable to string `begin = 'a'`
#### Function
```python
print_solution(P,D,Point)              # Printing all shortest path from start vertex to another vertex.
printPath(start,des,P,D,Point)         # Printing shortest path from start vertex to destination vertex which you setup above.
```

## Reference
[Randomized Speedup of the Bellman-Ford Algorithm](https://arxiv.org/abs/1111.5414)
