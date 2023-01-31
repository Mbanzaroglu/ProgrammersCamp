
numbers = [1,2,3,4,5]

numbersSquare = list(map(lambda num : num*num, numbers)) #square of each element in numbers will be placed in numbersSquare list.

numbersFiltered = list(filter(lambda num : num > 2, numbers)) #numbers greater than 2 in 'numbers' will be placed in numbersFiltered list.

from functools import reduce #reduce function is called from functools. 

numbersFactorial = reduce(lambda x,y : x*y, numbers)  #with each x*y is equal to x 

