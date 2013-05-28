import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: table identifier
    # value: order id
    key = record[0]
    value = record[1]  
    mr.emit_intermediate(value, record)

def reducer(key, joinedrows):
    # key: order id
    # value: row data
    orderdata = []
    listitemdata = []
    
    for row in joinedrows:
      if row[0] == 'order':
        orderdata.append(row)
      else:  
        listitemdata.append(row)
    
    for odrow in orderdata:
      for lidrow in listitemdata:
        mr.emit(odrow + lidrow)
    
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
