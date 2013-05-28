import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: nucleotides
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value, key)

def reducer(key, list_of_values):
    # key: sequenceid
    # value: nucleotide
    
    
    trimmed = key[:-10]
    distinct = set(trimmed)
    mr.emit(trimmed)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
