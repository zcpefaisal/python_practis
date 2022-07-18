
import mymodule

print(mymodule.test(2,3))

print(mymodule.add(2,3))

print(mymodule.sub(9,3))

print(mymodule.mul(2,3))

print(mymodule.div(10,2))



# other type calling 
from mymodule import *

print(test(2,3))

print(add(2,3))

print(sub(9,3))

print(mul(2,3))

print(div(10,2))