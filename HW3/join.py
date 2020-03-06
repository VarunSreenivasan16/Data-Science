import MapReduce
import sys

"""
JOIN in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(myList):
    id = myList[1]
    mr.emit_intermediate(id, myList)

# Implement the REDUCE function
def reducer(id, myList):
    

    for item in myList:
        if item[0] == "order":
            for item2 in myList:
                if item2[0] == "line_item":
                    
                    temp = ""
                    tempList = []
                    tempList = item + item2
                    mr.emit((tempList))
                   
    
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
