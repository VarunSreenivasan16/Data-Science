import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(myList):
    
    if(myList[0] == "a"):
        
        for k in range(0,5):
            mr.emit_intermediate((myList[1], k), [myList[0], myList[2], myList[3]])
        
    else:
        
        for k in range(0,5):
            mr.emit_intermediate(( k, myList[2]), [myList[0], myList[1], myList[3]])
        

# Implement the REDUCE function
def reducer(key, valList):
    
    (index1, index2) = key
    total = 0
    
    for i in range(0, 10):
       
        matrix = valList[i][0]
        index = valList[i][1]
        value = valList[i][2]
        
        for j in range(i+1, 10):
            if( matrix != valList[j][0] and index == valList[j][1]):
                total += value * valList[j][2]
    
    mr.emit((index1, index2, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
