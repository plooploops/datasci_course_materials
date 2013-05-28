import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record: [Matrix, i, j value]
    # matrix: a or b (from matrix a or matrix b)
    # i, j, value are integers
    # key: matrix
    # value: value
    # k: destination matrix col max, set 5
    # i: destination matrix row max, set 5
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if (matrix == 'a'):
      for k in range(5):
        mr.emit_intermediate((i, k),('a', j, value))
    else:
      for tempi in range(5):
        mr.emit_intermediate((tempi, j),('b', i, value))

def reducer(key, list_of_values):
    # key: destination row or column with original matrix
    # value: values
    
    avector = [elem[1] for elem in list_of_values if elem[0] == 'a']
    bvector = [elem[1] for elem in list_of_values if elem[0] == 'b']
    cvector = list(set(avector) & set(bvector))
    
    total = 0
    for val in cvector:
      aval = [elem[2] for elem in list_of_values if elem[0] == 'a' and elem[1] == val]
      bval = [elem[2] for elem in list_of_values if elem[0] == 'b' and elem[1] == val]
      total += aval[0] * bval[0]
    
    i = key[0]
    k = key[1]
    val = (i, k, total)
    mr.emit(val)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
