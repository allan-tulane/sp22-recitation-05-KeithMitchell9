from collections import defaultdict

def supersort(a, k):
    """
    The main sorting algorithm. You'll complete the
    three funcions count_values, get_positions, and construct_output.
    
    Params:
      a.....the input list
      k.....the maximum element in a
      
    Returns:
      sorted version a
    """
    counts = count_values(a, k)
    positions = get_positions(counts)
    return construct_output(a, positions)

def count_values(a, k):
  list1 = [0] * (k + 1)
  for i in a:
    list1[i] += 1
  return list1

def test_count_values():
    assert count_values([2,2,1,0,1,0,1,3], 3) == [2, 3, 2, 1]
    
def get_positions(counts):
  list2 = [0]
  temp_counts = scan(plus, 0, counts)
  counts = temp_counts[0]
  counts = counts[:-1]
  list2 += counts
  return list2
    
def test_get_positions():
    assert get_positions([2, 3, 2, 1]) == [0, 2, 5, 7]
    
def construct_output(a, positions):
  newlist = []
  count = count_values(a, max(a))
  for i in range(len(positions)):
    if count[i] != 0:
      newlist += [i] * count[i]
  return newlist

def test_construct_output():
    assert construct_output([2,2,1,0,1,0,1,3], [0, 2, 5, 7]) == [0,0,1,1,1,2,2,3]
    
def count_values_mr(a, k):
    """
    Use map-reduce to implement count_values.
    This is done; you'll have to complete count_map and count_reduce.
    """
    # done.
    int2count = dict(run_map_reduce(count_map, count_reduce, a))
    return [int2count.get(i,0) for i in range(k+1)]

def test_count_values_mr():
    assert count_values_mr([2,2,1,0,1,0,1,3], 3) == [2, 3, 2, 1]

def count_map(value):
  return [(value, 1)]

def count_reduce(group):
  return (group[0], reduce(plus, 0, group[1]))

# the below functions are provided for use above.

def run_map_reduce(map_f, reduce_f, mylist):
    # done. 
    pairs = flatten(list(map(map_f, mylist)))
    groups = collect(pairs)
    return [reduce_f(g) for g in groups]

def collect(pairs):
    # done.     
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())

def plus(x,y):
    # done. 
    return x + y


def scan(f, id_, a):
    # done. 
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        return f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
    
def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])
    
def flatten(sequences):
    return iterate(plus, [], sequences)
