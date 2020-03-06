import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Implement the MAP function
def mapper(myList):
    person_A = myList[0]
    person_B = myList[1]
    mr.emit_intermediate(person_A, 1)

# Implement the REDUCE function
def reducer(person_A, count_list):
    
    total = 0
    for v in count_list:
        total += v
    mr.emit((person_A, total))
   

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
