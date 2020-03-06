import MapReduce
import sys

"""
Inverted Index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(myList):
    document_id = myList[0]
    text = myList[1]
    text = text.split()
    tempList = []
    for t in text:
        
        if t not in tempList:
            tempList.append(t)
            mr.emit_intermediate(t, document_id)
            

# Implement the REDUCE function
def reducer(key, doc_id):
    
    mr.emit((key, doc_id))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
