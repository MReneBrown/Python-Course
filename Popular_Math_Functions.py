import math 

loss = -20.25    # floating point number
product_cost = 89.99   # floatiing point number

print(abs(loss))    # absolute value pure value-removes the negative "-" 
                    # Math library no needed for absolute
print(math.floor(product_cost))     # shows the value wanted the rounding down version
print(int(product_cost))            # will produce the same answer
print(math.ceil(product_cost))  
# drop decimal and always round up no matter what value is found after decimal
print(loss)
print(math.floor(loss)) 
# when floor is used value will be opposite as if it were a positive-lower for negative number
print(abs(math.floor(loss)))    # changes to positive number drops negative
print(round(product_cost))      # rounds to closest whole number
print(math.sqrt(product_cost))
print(math.pow(5, 2))   # equivalent to exponent diff is output-floating point number on math.pow
# math.pow function is much more complex/scientifically accurate
print(5 ** 2)       # exponent operator produces the integer

20.25
89
89
90
-20.25
-21
21
90
9.486305919587455
25.0
25

