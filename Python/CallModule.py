#%%
import Modules

print(Modules.multiply(2, 3))
#we called a function from "Modules.py" and used it
#%%

#we can assign a new variable for the external file name such as 

import Modules as m 

m.add(2,3)
m.multiply(2,3)
#it utilizes the usage
#%%
#lets try to call the dictionary 

print(m.customer["firstName"]) #we called the dictionary inside of the Module which is assigned as "m"
#%%
#'import Modules' code calles all of the Modules.py file. If want to call a specific function or class or items, we can call it like:,

from Modules import add #we just called the addition function 
print(add(2,3))
from Modules import customer #we just called the dictionary
print(customer["firstName"])

#%%