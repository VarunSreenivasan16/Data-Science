import MapReduce
import sys

"""
Assymetric Relationships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(myList):
    person_A = myList[0]
    person_B = myList[1]
    
    myList.sort()
    key = myList[0] + " " + myList[1]
    
    mr.emit_intermediate(key, [person_A, person_B] )
    
# Implement the REDUCE function
def reducer(key, myList):
    
    tempList = []
    if(len(myList) == 1):
        tempList.append(myList[0][1])
        tempList.append(myList[0][0])
        mr.emit(tempList)
    
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
